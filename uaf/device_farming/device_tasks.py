from datetime import datetime
from random import choice
from uuid import UUID, uuid4

from celery.schedules import crontab

from uaf.decorators.loggers.logger import log
from uaf.enums.device_status import DeviceStatus
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs
from uaf.utilities.appium.appium_utils import AppiumUtils
from uaf.utilities.database.mongo_utils import MongoUtility

from . import FilePaths, YamlParser, get_celery_app

app = get_celery_app()
config = YamlParser(FilePaths.COMMON)
mongo_client = MongoUtility(config.get_value("mongodb", "connection_string"))
mongo_client.client


def __get_unique_id() -> UUID:
    return uuid4()


@app.task
@log
def add_new_devices_to_list():
    """
    Adds newly connected devices to the device_stats collection with status available
    """
    all_devices = [
        __device_list["device_id"]
        for __device_list in mongo_client.find_many(config.get_value("mongodb", "device_stat_collection"))
    ]
    from platform import system

    if system().lower().__eq__("darwin"):
        connected_ios_physical_devices_list = AppiumUtils.fetch_connected_ios_devices_ids(
            MobileDeviceEnvironmentType.PHYSICAL
        )
        unique_ios_physical_devices_list = [
            device for device in connected_ios_physical_devices_list if device not in all_devices
        ]
        if unique_ios_physical_devices_list:
            mongo_client.insert_many(
                config.get_value("mongodb", "device_stat_collection"),
                [
                    {
                        "device_id": str(x),
                        "device_type": MobileDeviceEnvironmentType.PHYSICAL.value,
                        "device_os": MobileOs.IOS.value,
                        "status": DeviceStatus.AVAILABLE.value,
                    }
                    for x in unique_ios_physical_devices_list
                ],
            )
    connected_android_physical_devices_list = AppiumUtils.fetch_connected_android_devices_ids(
        MobileDeviceEnvironmentType.PHYSICAL
    )
    unique_android_physical_devices_list = [
        device for device in connected_android_physical_devices_list if device not in all_devices
    ]
    if unique_android_physical_devices_list:
        mongo_client.insert_many(
            config.get_value("mongodb", "device_stat_collection"),
            [
                {
                    "device_id": str(x),
                    "device_type": MobileDeviceEnvironmentType.PHYSICAL.value,
                    "device_os": MobileOs.ANDROID.value,
                    "status": DeviceStatus.AVAILABLE.value,
                }
                for x in unique_android_physical_devices_list
            ],
        )


@app.task
@log
def reserve_device(mobile_os: str):
    """
    Reserves random available device and updates status in database
    """
    available_devices = mongo_client.find_many(
        config.get_value("mongodb", "device_stat_collection"),
        {"status": DeviceStatus.AVAILABLE.value},
    )
    if not available_devices:
        raise ValueError(f"Failed to start any device for {mobile_os} mobile os as availability is 0!!")

    # randomly choose device_id based on the mobile os
    device_id = choice([device["device_id"] for device in available_devices if mobile_os.__eq__(device["device_os"])])
    uuid: UUID = __get_unique_id()
    session_doc = {
        "device_id": device_id,
        "start_time": datetime.utcnow().__str__(),
        "session_id": uuid,
        "device_os": mobile_os,
        "end_time": None,
    }
    device_stats_doc = {"$set": {"status": DeviceStatus.IN_USE.value}}
    mongo_client.update_one(
        config.get_value("mongodb", "device_stat_collection"),
        {"device_id": device_id},
        device_stats_doc,
    )
    mongo_client.insert_one(config.get_value("mongodb", "device_session_collection"), session_doc)
    return device_id, uuid


@app.task
@log
def release_device(device_id: str, session_id: UUID):
    """
    Releases device which is being requested and updates status in database
    """
    mongo_client.update_one(
        config.get_value("mongodb", "device_stat_collection"),
        {"device_id": device_id},
        {"$set": {"status": DeviceStatus.TERMINATED.value}},
    )
    mongo_client.update_one(
        config.get_value("mongodb", "device_session_collection"),
        {"session_id": str(session_id)},
        {"$set": {"end_time": datetime.utcnow().__str__()}},
    )


@app.task
@log
def check_device():
    """
    Fetch the list of devices from the database
    """
    terminated_device_docs = [
        __device_list["device_id"]
        for __device_list in mongo_client.find_many(
            config.get_value("mongodb", "device_stat_collection"),
            {"status": DeviceStatus.TERMINATED.value},
        )
    ]
    for device in terminated_device_docs:
        mongo_client.update_one(
            config.get_value("mongodb", "device_stat_collection"),
            {"device_id": device},
            {"$set": {"status": DeviceStatus.AVAILABLE.value}},
        )


app.conf.beat_schedule = {
    "update_device_availability": {
        "task": "uaf.device_farming.device_tasks.check_device",
        "schedule": crontab(minute="*/2"),
    },
    "add_new_device_to_device_list": {
        "task": "uaf.device_farming.device_tasks.add_new_devices_to_list",
        "schedule": crontab(minute="*/3"),
    },
}
