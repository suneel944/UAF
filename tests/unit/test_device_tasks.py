from pytest import mark, fixture
from unittest.mock import MagicMock, patch
from uuid import UUID

from uaf.device_farming.device_tasks import (
    add_new_devices_to_list,
    reserve_device,
    release_device,
    check_device,
)
from uaf.enums.device_status import DeviceStatus
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs


@fixture
def mock_mongo_client():
    return MagicMock()


@fixture
def mock_core_utils():
    return MagicMock()


@fixture
def mock_config():
    config = MagicMock()
    config.get_value.return_value = "test_collection"
    return config


@mark.unit_test
@patch("uaf.device_farming.device_tasks.mongo_client", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.CoreUtils", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.config", new_callable=MagicMock)
@patch("platform.system")
def test_add_new_devices_to_list(
    mock_system, mock_config, mock_core_utils, mock_mongo_client
):
    mock_system.return_value = "Linux"
    mock_mongo_client.find_many.return_value = [{"device_id": "existing_device"}]
    mock_core_utils.fetch_connected_android_devices_ids.return_value = [
        "new_device",
        "existing_device",
    ]

    add_new_devices_to_list()

    # Adjust the expectation to use the config mock instead of hardcoded "test_collection"
    mock_mongo_client.insert_many.assert_called_once_with(
        mock_config.get_value(),  # Use the mock config's get_value()
        [
            {
                "device_id": "new_device",
                "device_type": MobileDeviceEnvironmentType.PHYSICAL.value,
                "device_os": MobileOs.ANDROID.value,
                "status": DeviceStatus.AVAILABLE.value,
            }
        ],
    )


@mark.unit_test
@patch("uaf.device_farming.device_tasks.mongo_client", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.config", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.choice")
@patch("uaf.device_farming.device_tasks.__get_unique_id")
def test_reserve_device(
    mock_get_unique_id, mock_choice, mock_config, mock_mongo_client
):
    mock_mongo_client.find_many.return_value = [
        {"device_id": "device1", "device_os": "android"},
        {"device_id": "device2", "device_os": "ios"},
    ]
    mock_choice.return_value = "device1"
    mock_get_unique_id.return_value = UUID("12345678-1234-5678-1234-567812345678")

    device_id, uuid = reserve_device("android")

    assert device_id == "device1"
    assert uuid == UUID("12345678-1234-5678-1234-567812345678")
    mock_mongo_client.update_one.assert_called_once()
    mock_mongo_client.insert_one.assert_called_once()


@mark.unit_test
@patch("uaf.device_farming.device_tasks.mongo_client", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.config", new_callable=MagicMock)
def test_release_device(mock_config, mock_mongo_client):
    device_id = "test_device"
    session_id = UUID("12345678-1234-5678-1234-567812345678")

    release_device(device_id, session_id)

    assert mock_mongo_client.update_one.call_count == 2


@mark.unit_test
@patch("uaf.device_farming.device_tasks.mongo_client", new_callable=MagicMock)
@patch("uaf.device_farming.device_tasks.config", new_callable=MagicMock)
def test_check_device(mock_config, mock_mongo_client):
    mock_mongo_client.find_many.return_value = [
        {"device_id": "device1"},
        {"device_id": "device2"},
    ]

    check_device()

    assert mock_mongo_client.update_one.call_count == 2
    # Adjust the expectation to use the config mock instead of hardcoded "test_collection"
    mock_mongo_client.update_one.assert_called_with(
        mock_config.get_value(),  # Use the mock config's get_value()
        {"device_id": "device2"},
        {"$set": {"status": DeviceStatus.AVAILABLE.value}},
    )
