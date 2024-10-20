from pytest import mark, fixture
from unittest.mock import MagicMock, patch
from uaf.utilities.database.postgres_utility import PostgresUtility


@fixture
def mock_psycopg_connect():
    with patch(
        "uaf.utilities.database.postgres_utility.psycopg.connect"
    ) as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        yield mock_connect


@fixture
def postgres_utility(mock_psycopg_connect):
    return PostgresUtility("mock_connection_string")


@mark.unit_test
def test_postgres_utility_init(postgres_utility, mock_psycopg_connect):
    assert postgres_utility.connection_string == "mock_connection_string"
    mock_psycopg_connect.assert_called_once_with("mock_connection_string")
    assert postgres_utility.conn.autocommit is True


@mark.unit_test
def test_postgres_utility_context_manager(mock_psycopg_connect):
    with PostgresUtility("mock_connection_string") as pu:
        assert isinstance(pu, PostgresUtility)
    mock_psycopg_connect.return_value.close.assert_called_once()


@mark.unit_test
def test_postgres_utility_connect(postgres_utility, mock_psycopg_connect):
    postgres_utility.conn.closed = True
    postgres_utility.connect()
    assert mock_psycopg_connect.call_count == 2  # Once in __init__, once in connect


@mark.unit_test
def test_postgres_utility_disconnect(postgres_utility):
    postgres_utility.disconnect()
    postgres_utility.conn.close.assert_called_once()


@mark.unit_test
def test_postgres_utility_ping(postgres_utility):
    mock_cursor = MagicMock()
    postgres_utility.conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (1,)

    result = postgres_utility.ping()
    assert result == (1,)
    mock_cursor.execute.assert_called_once_with("SELECT 1")


@mark.unit_test
def test_postgres_utility_execute(postgres_utility):
    postgres_utility.execute("INSERT INTO test_table VALUES (%s, %s)", (1, "test"))
    postgres_utility.conn.cursor.return_value.__enter__.return_value.execute.assert_called_once_with(
        "INSERT INTO test_table VALUES (%s, %s)", (1, "test")
    )


@mark.unit_test
def test_postgres_utility_fetch_one(postgres_utility):
    mock_cursor = MagicMock()
    postgres_utility.conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {"id": 1, "name": "test"}

    result = postgres_utility.fetch_one("SELECT * FROM test_table WHERE id = %s", (1,))
    assert result == {"id": 1, "name": "test"}
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM test_table WHERE id = %s", (1,)
    )


@mark.unit_test
def test_postgres_utility_fetch_many(postgres_utility):
    mock_cursor = MagicMock()
    postgres_utility.conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {"id": 1, "name": "test1"},
        {"id": 2, "name": "test2"},
    ]

    result = postgres_utility.fetch_many("SELECT * FROM test_table")
    assert result == [{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]
    mock_cursor.execute.assert_called_once_with("SELECT * FROM test_table", None)


@mark.unit_test
def test_postgres_utility_modify(postgres_utility):
    postgres_utility.modify(
        "UPDATE test_table SET name = %s WHERE id = %s", ("new_name", 1)
    )
    postgres_utility.conn.cursor.return_value.__enter__.return_value.execute.assert_called_once_with(
        "UPDATE test_table SET name = %s WHERE id = %s", ("new_name", 1)
    )


@mark.unit_test
def test_postgres_utility_modify_many(postgres_utility):
    params_list = [(1, "test1"), (2, "test2")]
    postgres_utility.modify_many("INSERT INTO test_table VALUES (%s, %s)", params_list)
    postgres_utility.conn.cursor.return_value.__enter__.return_value.executemany.assert_called_once_with(
        "INSERT INTO test_table VALUES (%s, %s)", params_list
    )
