from typing import Any, List, Optional

from pymongo import MongoClient
from pymongo.errors import CollectionInvalid, ConnectionFailure, OperationFailure


class MongoUtility:
    def __init__(self, connection_string, pool_size=10, uuid_representation="standard"):
        self._client = None
        self.connection_string = connection_string
        self.pool_size = pool_size
        self._database = None
        self.collections = {}
        self._uuid_representation = uuid_representation

    def __enter__(self) -> "MongoUtility":
        """
        Enter method to support the with statement
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit method to support the with statement
        """
        self.disconnect()
        self._client = None
        self._database = None

    def ping(self):
        if self._database is not None:
            return self._database.command("ping")

    @property
    def client(self):
        if not self._client:
            self.connect()
        return self._client

    @property
    def database(self):
        if self._client is not None:
            self._database = self._client.get_default_database()
        return self._database

    @property
    def current_database(self):
        """
        Returns the current active database name in focus
        """
        if self._database is not None:
            return self._database.name
        raise ValueError("current database is not set! or client connection is not made")

    @property
    def uuid_representation(self):
        """
        Returns the uuid representation of active instance in focus
        """
        if self._uuid_representation is not None:
            return self._uuid_representation

    @property
    def current_collections(self):
        """
        Returns current collection list in instance
        """
        if self.collections is not None:
            return self.collections
        raise ValueError("current collection is not set! or client connection is not made")

    def create_database(self, database_name: str, **kwargs: Any):
        try:
            if database_name in self.fetch_database_names():
                raise ValueError(f"Database '{database_name}' already exists!")
            else:
                if self._client is not None:
                    db = self._client[database_name]
                    db = db[kwargs.get("collection_name", "to_be_deleted_collection")]
                    db.insert_one({})
        except Exception as e:
            raise ValueError(f"Failed to create database: {e}")

    def delete_database(self, database_name: str):
        try:
            if self._client is not None:
                self._client.drop_database(database_name)
        except OperationFailure as e:
            raise ValueError(f"Failed to delete database: {e}")

    def delete_collection(self, collection_name: str):
        try:
            if self._database is not None:
                self._database.drop_collection(collection_name)
            if collection_name in self.collections:
                self.collections.pop(collection_name)
        except OperationFailure as e:
            raise ValueError(f"Failed to delete collection: {e}")

    def connect(self):
        try:
            self._client = MongoClient(
                self.connection_string,
                maxPoolSize=self.pool_size,
                uuidRepresentation=self._uuid_representation,
            )
            self._database = self._client.get_default_database()
        except ConnectionFailure as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def disconnect(self):
        if self._client is not None:
            self._client.close()
            self._client = None
        self._database = None

    def get_collection(self, collection_name: str):
        collection = None
        if collection_name not in self.collections.keys():
            try:
                if self._database is not None:
                    collection = self._database[collection_name]
                    self.collections[collection_name] = collection
            except CollectionInvalid as e:
                raise ValueError(f"Failed to get collection: {e}")
        else:
            collection = self.collections[collection_name]
        return collection

    def create_collection(self, collection_name: str, **kwargs: Any):
        try:
            if self._database is not None:
                self._database.create_collection(collection_name, **kwargs)
        except CollectionInvalid as e:
            raise ValueError(f"Error creating collection: {e}")

    def fetch_collection_names(self):
        try:
            if self._database is not None:
                return self._database.list_collection_names()
        except OperationFailure as e:
            raise ValueError(f"Failed to get collection names list: {e}")

    def fetch_database_names(self):
        try:
            if self._client is not None:
                return self._client.list_database_names()
        except OperationFailure as e:
            raise ValueError(f"Failed to get database names list: {e}")

    def insert_one(self, collection_name: str, document: dict[str, Any], **kwargs: Any):
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_one(document, **kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to insert document: {e}")

    def insert_many(self, collection_name: str, documents: List[dict[str, Any]], **kwargs: Any):
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_many(documents, **kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to insert documents: {e}")

    def find_one(
        self,
        collection_name: str,
        filter: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        try:
            collection = self.get_collection(collection_name)
            return collection.find_one(filter, **kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to find document: {e}")

    def find_one_and_replace(
        self,
        collection_name: str,
        filter: dict[str, Any],
        replacement: dict[str, Any],
        **kwargs: Any,
    ):
        try:
            self.get_collection(collection_name).find_one_and_replace(filter, replacement, kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to find and replace document: {e}")

    def find_many(
        self,
        collection_name: str,
        filter: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        try:
            collection = self.get_collection(collection_name)
            cursor = collection.find(filter, **kwargs)
            return [doc for doc in cursor]
        except OperationFailure as e:
            raise ValueError(f"Failed to find documents: {e}")

    def update_one(
        self,
        collection_name: str,
        filter: dict[str, Any],
        update: dict[str, Any],
        **kwargs: Any,
    ):
        try:
            collection = self.get_collection(collection_name)
            return collection.update_one(filter, update, **kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to update document: {e}")

    def update_many(
        self,
        collection_name: str,
        filter: dict[str, Any],
        update: dict[str, Any],
        **kwargs: Any,
    ):
        try:
            collection = self.get_collection(collection_name)
            return collection.update_many(filter, update, **kwargs)
        except OperationFailure as e:
            raise ValueError(f"Failed to update documents: {e}")

    def delete_one(self, collection_name: str, filter: dict[str, Any]):
        try:
            collection = self.get_collection(collection_name)
            collection.delete_one(filter)
        except OperationFailure as e:
            raise ValueError(f"Failed to delete document: {e}")

    def delete_many(self, collection_name: str, filter: dict[str, Any]):
        try:
            collection = self.get_collection(collection_name)
            collection.delete_many(filter)
        except OperationFailure as e:
            raise ValueError(f"Failed to delete documents: {e}")
