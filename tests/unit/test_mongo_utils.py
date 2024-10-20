from pytest import mark, fixture
from unittest.mock import MagicMock, patch
from pymongo.errors import ConnectionFailure, OperationFailure

from uaf.utilities.database.mongo_utils import MongoUtility


@fixture
def mock_mongo_client():
    with patch("uaf.utilities.database.mongo_utils.MongoClient") as mock_client:
        yield mock_client


@mark.unit_test
def test_mongo_utility_init():
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    assert mongo_util.connection_string == "mongodb://localhost:27017/testdb"
    assert mongo_util.pool_size == 10
    assert mongo_util.uuid_representation == "standard"


@mark.unit_test
def test_mongo_utility_connect(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()
    mock_mongo_client.assert_called_once_with(
        "mongodb://localhost:27017/testdb",
        maxPoolSize=10,
        uuidRepresentation="standard",
    )


@mark.unit_test
def test_mongo_utility_connect_failure(mock_mongo_client):
    mock_mongo_client.side_effect = ConnectionFailure("Connection failed")
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    try:
        mongo_util.connect()
    except ConnectionFailure as e:
        assert str(e) == "Failed to connect to MongoDB: Connection failed"


@mark.unit_test
def test_mongo_utility_disconnect(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()
    mongo_util.disconnect()
    mock_mongo_client.return_value.close.assert_called_once()


@mark.unit_test
def test_mongo_utility_insert_one(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()

    mock_collection = MagicMock()
    mock_mongo_client.return_value.get_default_database.return_value.__getitem__.return_value = (
        mock_collection
    )

    document = {"name": "John Doe", "age": 30}
    mongo_util.insert_one("test_collection", document)

    mock_collection.insert_one.assert_called_once_with(document)


@mark.unit_test
def test_mongo_utility_find_one(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()

    mock_collection = MagicMock()
    mock_mongo_client.return_value.get_default_database.return_value.__getitem__.return_value = (
        mock_collection
    )

    filter_query = {"name": "John Doe"}
    mongo_util.find_one("test_collection", filter_query)

    mock_collection.find_one.assert_called_once_with(filter_query)


@mark.unit_test
def test_mongo_utility_update_one(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()

    mock_collection = MagicMock()
    mock_mongo_client.return_value.get_default_database.return_value.__getitem__.return_value = (
        mock_collection
    )

    filter_query = {"name": "John Doe"}
    update_data = {"$set": {"age": 31}}
    mongo_util.update_one("test_collection", filter_query, update_data)

    mock_collection.update_one.assert_called_once_with(filter_query, update_data)


@mark.unit_test
def test_mongo_utility_delete_one(mock_mongo_client):
    mongo_util = MongoUtility("mongodb://localhost:27017/testdb")
    mongo_util.connect()

    mock_collection = MagicMock()
    mock_mongo_client.return_value.get_default_database.return_value.__getitem__.return_value = (
        mock_collection
    )

    filter_query = {"name": "John Doe"}
    mongo_util.delete_one("test_collection", filter_query)

    mock_collection.delete_one.assert_called_once_with(filter_query)
