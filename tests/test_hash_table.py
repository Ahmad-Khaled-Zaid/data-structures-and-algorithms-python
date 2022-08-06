import pytest
from hash_table.hash_table import HashTable


def test_instantiate_hash_table(hash_table_1):
    actual = hash_table_1.size
    expected = 1024
    assert actual == expected


def test_contains(hash_table_1):
    actual = hash_table_1.contains("ahmad")
    expected = True
    assert actual == expected


def test_keys(hash_table_1):
    actual = hash_table_1.keys()
    expected = ["ahmad", "sara", "Mohammed"]
    assert actual == expected


def test_set(hash_table_1):
    hash_table_1.set("ali", "grey")
    actual = hash_table_1.contains("ali")
    expected = True
    assert actual == expected


def test_get(hash_table_1):
    actual = hash_table_1.get("sara")
    expected = "red"
    assert actual == expected


def test_hash(hash_table_1):
    actual = hash_table_1._HashTable__hash("ABC")
    expected = 56034 % 1024
    assert actual == expected


@pytest.fixture
def hash_table_1():
    hash_table = HashTable()
    hash_table.set("ahmad", "green")
    hash_table.set("sara", "red")
    hash_table.set("Mohammed", "blue")
    return hash_table
