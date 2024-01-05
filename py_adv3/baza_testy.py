import pytest
import sqlite3


@pytest.fixture(params=[':memory:'])
def connection(request):
    return sqlite3.connect(request.param)


@pytest.yield_fixture
def transaction(connection):
    with connection:
        yield connection


def test_insert(transaction):
    transaction.execute('CREATE TABLE test (id integer)')
    transaction.execute('INSERT INTO test VALUES (1),(2),(3)')
