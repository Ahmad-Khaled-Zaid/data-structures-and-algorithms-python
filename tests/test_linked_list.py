import pytest
from Linked_List.linked_list import LinkedList


def test_create_list(new_list):
    assert new_list


def test_insert(new_list):
    assert new_list.current


def test_head_is_first_node(new_list):
    assert new_list.head.value == 10


def test_insert_multiple_value(new_list):
    assert new_list.head.next.value == 5


def test_is_exists(new_list):
    assert new_list.includes(5) == True


def test_not_exists(new_list):
    assert new_list.includes(20) == False


def test_values_collections(new_list):
    assert new_list.to_string() == " { 10 } ->  { 5 } ->  { 4 } -> Null"


@pytest.fixture
def new_list():
    list_1 = LinkedList()
    list_1.insert_first(4)
    list_1.insert_first(5)
    list_1.insert_first(10)
    return list_1



