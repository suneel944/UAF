from celery import Celery

from uaf.enums.file_paths import FilePaths
from uaf.utilities.parser.yaml_parser_utils import YamlParser

__all__ = ["FilePaths", "YamlParser"]


def get_celery_app():
    config = YamlParser(FilePaths.COMMON)
    celery_app = Celery(
        "device_farm",
        broker=config.get_value("celery", "broker_url"),
        backend=config.get_value("celery", "result_backend"),
    )
    return celery_app
