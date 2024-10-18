import psycopg
from typing import Any


class PostgresUtility:
    def __init__(self, connection_string: str):
        """
        Constructor for PostgresUtility class.

        Args:
            connection_string (str): PostgreSQL connection string
        """
        self.connection_string = connection_string
        self.conn = psycopg.connect(connection_string)
        self.conn.autocommit = True

    def __enter__(self) -> "PostgresUtility":
        """
        Support for the with statement to automatically manage resources.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit method for context manager to close connections.
        """
        self.disconnect()

    def connect(self):
        """
        Reconnect to PostgreSQL if the connection is closed.
        """
        if self.conn.closed:
            self.conn = psycopg.connect(self.connection_string)
            self.conn.autocommit = True

    def disconnect(self):
        """
        Close the connection to PostgreSQL.
        """
        if self.conn:
            self.conn.close()

    def ping(self) -> tuple[Any, ...] | None:
        """
        Ping the database to ensure connection is live.

        Returns:
            Optional[tuple[Any, ...]]: The result of the ping query or None if no rows are returned.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result is not None:
                return tuple(result)
            return None

    def execute(self, query: str, params: tuple[Any, ...] | None = None) -> None:
        """
        General method to execute a SQL query (INSERT, UPDATE, DELETE) without expecting any result.

        Args:
            query (str): The SQL query to execute.
            params (Optional[tuple[Any, ...]]): Parameters for the query.
        """
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)

    def fetch_one(
        self, query: str, params: tuple[Any, ...] | None = None
    ) -> dict[str, Any] | None:
        """
        Fetch a single row from the database.

        Args:
            query (str): The SQL SELECT query.
            params (Optional[tuple[Any, ...]]): Parameters for the query.

        Returns:
            Optional[dict[str, Any]]: A single row as a dictionary or None if no rows are found.
        """
        with self.conn.cursor(row_factory=psycopg.rows.dict_row) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result if result is not None else None

    def fetch_many(
        self, query: str, params: tuple[Any, ...] | None = None
    ) -> list[dict[str, Any]]:
        """
        Fetch multiple rows from the database.

        Args:
            query (str): The SQL SELECT query.
            params (Optional[tuple[Any, ...]]): Parameters for the query.

        Returns:
            list[dict[str, Any]]: A list of rows as dictionaries.
        """
        with self.conn.cursor(row_factory=psycopg.rows.dict_row) as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results if results is not None else []

    def modify(self, query: str, params: tuple[Any, ...] | None = None) -> None:
        """
        Generalized method to perform INSERT, UPDATE, or DELETE operations.

        Args:
            query (str): The SQL query to execute (INSERT, UPDATE, DELETE).
            params (Optional[tuple[Any, ...]]): Parameters for the query.
        """
        self.execute(query, params)

    def modify_many(self, query: str, params_list: list[tuple[Any, ...]]) -> None:
        """
        Generalized method to perform batch INSERT, UPDATE, or DELETE operations.

        Args:
            query (str): The SQL query to execute.
            params_list (list[tuple[Any, ...]]): List of parameter tuples for the query.
        """
        with self.conn.cursor() as cursor:
            cursor.executemany(query, params_list)
