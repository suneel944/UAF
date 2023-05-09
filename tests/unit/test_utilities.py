from pytest import mark, raises

from uaf.decorators.pytest.pytest_ordering import order
from uaf.enums.file_paths import FilePaths
from uaf.utilities.database.mongo_utils import MongoUtility
from uaf.utilities.parser.yaml_parser_utils import YamlParser

config = YamlParser(FilePaths.COMMON)
connection_string = config.get_value("mongodb", "connection_string")


@mark.skip(reason="Skipping it because, the mongo infra setup code is not ready")
@mark.unit_test
@order(1)
def test_mongo_db_connectivity():
    with MongoUtility(connection_string) as mongo_client:
        assert "ok" in mongo_client.ping()


@mark.skip(reason="Skipping it because, the mongo infra setup code is not ready")
@mark.unit_test
@order(2)
def test_mongo_db_creation():
    with MongoUtility(connection_string) as mongo_client:
        mongo_client.create_database("test-database")
        assert "test-database" in [y for y in mongo_client.fetch_database_names()]


@mark.skip(reason="Skipping it because, the mongo infra setup code is not ready")
@mark.unit_tests
@order(3)
def test_mongo_db_deletion():
    with MongoUtility(connection_string) as mongo_client:
        if "test-database" not in [y for y in mongo_client.fetch_database_names()]:
            mongo_client.create_database("test-database")
        mongo_client.delete_database("test-database")
        assert "test-database" not in [y for y in mongo_client.fetch_database_names()]


@mark.skip(reason="Skipping it because, the mongo infra setup code is not ready")
@mark.unit_test
@order(4)
def test_mongo_db_duplicate_database_creation():
    with MongoUtility(connection_string) as mongo_client:
        import random

        db_list = mongo_client.fetch_database_names()
        rand_choice = random.choice(db_list)
        with raises(ValueError) as exc_info:
            mongo_client.create_database(rand_choice)
        assert str(exc_info.value).__contains__(f"Database '{rand_choice}' already exists!")
