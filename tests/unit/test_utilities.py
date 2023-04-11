import pytest
from uaf.decorators.pytest.pytest_ordering import order
from uaf.utilities.database.mongo_utils import MongoUtility
from uaf.utilities.parser.yaml_parser_utils import YamlParser
from uaf.enums.file_paths import FilePaths


config = YamlParser(FilePaths.COMMON)
connection_string = config.get_value("mongodb", "connection_string")


@order(1)
def test_mongo_db_connectivity():
    with MongoUtility(connection_string) as mongo_client:
        assert "ok" in mongo_client.ping()


@order(2)
def test_mongo_db_creation():
    with MongoUtility(connection_string) as mongo_client:
        mongo_client.create_database("test-database")
        assert "test-database" in [y for y in mongo_client.fetch_database_names()]


@order(3)
def test_mongo_db_deletion():
    with MongoUtility(connection_string) as mongo_client:
        if "test-database" not in [y for y in mongo_client.fetch_database_names()]:
            mongo_client.create_database("test-database")
        mongo_client.delete_database("test-database")
        assert "test-database" not in [y for y in mongo_client.fetch_database_names()]


@order(4)
def test_mongo_db_duplicate_database_creation():
    with MongoUtility(connection_string) as mongo_client:
        import random

        db_list = mongo_client.fetch_database_names()
        rand_choice = random.choice(db_list)
        with pytest.raises(ValueError) as exc_info:
            mongo_client.create_database(rand_choice)
        assert str(exc_info.value).__contains__(
            f"Database '{rand_choice}' already exists!"
        )
