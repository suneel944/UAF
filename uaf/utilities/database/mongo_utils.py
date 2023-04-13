from typing import Any, List, Optional

from pymongo import MongoClient
from pymongo.errors import CollectionInvalid, ConnectionFailure, OperationFailure


class MongoUtility:
    def __init__(self, connection_string, pool_size=10, uuid_representation="standard"):
        """constructor

        Args:
            connection_string (_type_): connection string - format : mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
            pool_size (int, optional): max connection that can be open at the same time between application and mongodb. Defaults to 10.
            uuid_representation (str, optional): uuid representation value. Defaults to "standard".
        """
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
        """Exit method to support the with statement

        Args:
            exc_type (_type_): exception type
            exc_val (_type_): exception value
            exc_tb (_type_): exception traceback
        """
        self.disconnect()
        self._client = None
        self._database = None

    def ping(self):
        """Test connection to the mongodb database"""
        if self._database is not None:
            return self._database.command("ping")

    @property
    def client(self):
        """Provides mongodb client instance

        Returns:
            MongoClient: mongo client instance
        """
        if not self._client:
            self.connect()
        return self._client

    @property
    def database(self):
        """Fetches the default database

        Returns:
            Database: Database instance
        """
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
        """Creates a new database with a dummy collection

        Args:
            database_name (str): name of the database

        Raises:
            ValueError: if failed to create database/database already exists
        """
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
        """Delete a database

        Args:
            database_name (str): name of the database

        Raises:
            OperationFailure: if failed to delete database
        """
        try:
            if self._client is not None:
                self._client.drop_database(database_name)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to delete database: {e}")

    def delete_collection(self, collection_name: str):
        """Deletes a collection in active database in focus

        Args:
            collection_name (str): name of the collection

        Raises:
            OperationFailure: if failed to delete collection
        """
        try:
            if self._database is not None:
                self._database.drop_collection(collection_name)
            if collection_name in self.collections:
                self.collections.pop(collection_name)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to delete collection: {e}")

    def connect(self):
        """Connect to default database

        Raises:
            ConnectionFailure: if failed to connect to mongodb
        """
        try:
            self._client = MongoClient(
                self.connection_string,
                maxPoolSize=self.pool_size,
                uuidRepresentation=self._uuid_representation,
            )
            self._database = self._client.get_default_database()
        except ConnectionFailure as e:
            raise ConnectionFailure(f"Failed to connect to MongoDB: {e}")

    def disconnect(self):
        """Disconnects from mongo database"""
        if self._client is not None:
            self._client.close()
            self._client = None
        self._database = None

    def get_collection(self, collection_name: str):
        """Fetches collection from current active database

        Args:
            collection_name (str): name of collection

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        collection = None
        if collection_name not in self.collections.keys():
            try:
                if self._database is not None:
                    collection = self._database[collection_name]
                    self.collections[collection_name] = collection
            except CollectionInvalid as e:
                raise CollectionInvalid(f"Failed to get collection: {e}")
        else:
            collection = self.collections[collection_name]
        return collection

    def create_collection(self, collection_name: str, **kwargs: Any):
        try:
            if self._database is not None:
                self._database.create_collection(collection_name, **kwargs)
        except CollectionInvalid as e:
            raise CollectionInvalid(f"Error creating collection: {e}")

    def fetch_collection_names(self):
        try:
            if self._database is not None:
                return self._database.list_collection_names()
        except OperationFailure as e:
            raise OperationFailure(f"Failed to get collection names list: {e}")

    def fetch_database_names(self):
        """Fetches database name list from the current mongoclient instance

        Raises:
            OperationFailure: if failed to get database names list

        Returns:
            list[str]: list of document names
        """
        try:
            if self._client is not None:
                return self._client.list_database_names()
        except OperationFailure as e:
            raise OperationFailure(f"Failed to get database name list: {e}")

    def insert_one(self, collection_name: str, document: dict[str, Any], **kwargs: Any):
        """Insert one document in the given collection of current active database in focus

        Args:
            collection_name (str): name of the collection
            document (dict[str, Any]): unit document

        Raises:
            OperationFailure: if failed to insert document

        Returns:
            InsertOneResult: insertion result status
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_one(document, **kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to insert document: {e}")

    def insert_many(self, collection_name: str, documents: List[dict[str, Any]], **kwargs: Any):
        """Inserts one or more documents in the given collection of current active database in focus

        Args:
            collection_name (str): name of the collection
            documents (List[dict[str, Any]]): list documents that needs to be inserted

        Raises:
            OperationFailure: if failed to insert documents

        Returns:
            InsertManyResult: data insertions result
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_many(documents, **kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to insert documents: {e}")

    def find_one(
        self,
        collection_name: str,
        filter: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        """Fetches a document with respect to filter query provided

        Args:
            collection_name (str): name of the collection
            filter (Optional[dict[str, Any]], optional): filter query. Defaults to None.

        Raises:
            OperationFailure: if failed to find a document

        Returns:
            _DocumentType: a single document
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.find_one(filter, **kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to find document: {e}")

    def find_one_and_replace(
        self,
        collection_name: str,
        filter: dict[str, Any],
        replacement: dict[str, Any],
        **kwargs: Any,
    ):
        """Fetches a document with respect to filter query provided and replaces it with replacement document

        Args:
            collection_name (str): name of the collection
            filter (dict[str, Any]): filter query
            replacement (dict[str, Any]): replacement document

        Raises:
            OperationFailure: if failed to find and replace document
        """
        try:
            self.get_collection(collection_name).find_one_and_replace(filter, replacement, kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to find and replace document: {e}")

    def find_many(
        self,
        collection_name: str,
        filter: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        """Fetches list of documents with respect to filter query provided

        Args:
            collection_name (str): name of the collection
            filter (Optional[dict[str, Any]], optional): filter query. Defaults to None.

        Raises:
            OperationFailure: if failed to find documents

        Returns:
            list[Cursor[_DocumentType]]: list of matching documents
        """
        try:
            collection = self.get_collection(collection_name)
            cursor = collection.find(filter, **kwargs)
            return [doc for doc in cursor]
        except OperationFailure as e:
            raise OperationFailure(f"Failed to find documents: {e}")

    def update_one(
        self,
        collection_name: str,
        filter: dict[str, Any],
        update: dict[str, Any],
        **kwargs: Any,
    ):
        """Updates a filtered document from a collection

        Args:
            collection_name (str): name of the collection
            filter (dict[str, Any]): filter query
            update (dict[str, Any]): update data

        Raises:
            OperationFailure: if failed to update document

        Returns:
            UpdateResult: update result status
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.update_one(filter, update, **kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to update document: {e}")

    def update_many(
        self,
        collection_name: str,
        filter: dict[str, Any],
        update: dict[str, Any],
        **kwargs: Any,
    ):
        """Updates one or more filtered documents from a collection

        Args:
            collection_name (str): name of the collection
            filter (dict[str, Any]): filter query
            update (dict[str, Any]): update data

        Raises:
            OperationFailure: if failed to update documents

        Returns:
            UpdateResult: update result status
        """
        try:
            collection = self.get_collection(collection_name)
            return collection.update_many(filter, update, **kwargs)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to update documents: {e}")

    def delete_one(self, collection_name: str, filter: dict[str, Any]):
        try:
            collection = self.get_collection(collection_name)
            collection.delete_one(filter)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to delete document: {e}")

    def delete_many(self, collection_name: str, filter: dict[str, Any]):
        """Deletes one or more filtered documents from a collection

        Args:
            collection_name (str): name of the collection
            filter (dict[str, Any]): filter query

        Raises:
            OperationFailure: if failed to delete document
        """
        try:
            collection = self.get_collection(collection_name)
            collection.delete_many(filter)
        except OperationFailure as e:
            raise OperationFailure(f"Failed to delete documents: {e}")
