import pytest
from Linked_List.linked_list import LinkedList


def test_create_list(new_list):
    assert new_list


def test_insert(new_list):
    assert new_list.current is None


def test_head_is_first_node(new_list):
    assert new_list.head.value == 4


def test_insert_multiple_value(new_list):
    assert new_list.head.next.value == 5


def test_is_exists(new_list):
    assert new_list.includes(5) is True


def test_not_exists(new_list):
    assert new_list.includes(20) is False


def test_values_collections(new_list):
    assert new_list.to_string() == " { 4 } -> { 5 } -> { 10 } -> Null"


def test_values_insert_last_case1(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    newer_list.insert_last(5)
    assert newer_list.to_string() == " { 1 } -> { 3 } -> { 2 } -> { 5 } -> Null"


def test_values_insert_last_case2(newer_list):
    newer_list.insert_last(1)
    assert newer_list.to_string() == " { 1 } -> Null"


#
#
def test_values_insert_before_case1(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    newer_list.insert_before(3, 5)
    assert newer_list.to_string() == " { 1 } -> { 5 } -> { 3 } -> { 2 } -> Null"


#
def test_values_insert_before_case2(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    newer_list.insert_before(1, 5)
    assert newer_list.to_string() == " { 5 } -> { 1 } -> { 3 } -> { 2 } -> Null"


#
def test_values_insert_before_case3(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(2)
    newer_list.insert_last(2)
    newer_list.insert_before(2, 5)
    assert newer_list.to_string() == " { 1 } -> { 5 } -> { 2 } -> { 2 } -> Null"


#
def test_values_insert_before_case4(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    with pytest.raises(Exception):
        newer_list.insert_before(4, 5)


def test_values_insert_after_case1(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    newer_list.insert_after(3, 5)
    assert newer_list.to_string() == " { 1 } -> { 3 } -> { 5 } -> { 2 } -> Null"


def test_values_insert_after_case2(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    newer_list.insert_after(2, 5)
    assert newer_list.to_string() == " { 1 } -> { 3 } -> { 2 } -> { 5 } -> Null"


def test_values_insert_after_case3(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(2)
    newer_list.insert_last(2)
    newer_list.insert_after(2, 5)
    assert newer_list.to_string() == " { 1 } -> { 2 } -> { 5 } -> { 2 } -> Null"


def test_values_insert_after_case4(newer_list):
    newer_list.insert_last(1)
    newer_list.insert_last(3)
    newer_list.insert_last(2)
    with pytest.raises(Exception):
        newer_list.insert_after(4, 5)


def test_length_case1(new_list):
    assert new_list.length == 3


def test_length_case2(new_list):
    new_list.insert_before(5, 23)
    new_list.insert_after(4, 78)
    new_list.insert_last(99)
    assert new_list.length == 6


def test_insert_middle_case1(new_list):
    new_list.insert_in_middle(11)
    assert new_list.to_string() == " { 4 } -> { 5 } -> { 11 } -> { 10 } -> Null"


def test_insert_middle_case2(newer_list):
    newer_list.insert_in_middle(11)
    assert newer_list.to_string() == " Null"


def test_insert_middle_case3(new_list):
    new_list.insert_last(31)
    new_list.insert_in_middle(70)
    assert new_list.to_string() == " { 4 } -> { 5 } -> { 70 } -> { 10 } -> { 31 } -> Null"


def test_insert_middle_case4(newer_list):
    newer_list.insert_last(31)
    newer_list.insert_in_middle(70)
    assert newer_list.to_string() == " { 31 } -> { 70 } -> Null"


@pytest.fixture
def new_list():
    list_1 = LinkedList()
    list_1.insert_first(10)
    list_1.insert_first(5)
    list_1.insert_first(4)
    return list_1


@pytest.fixture
def newer_list():
    list_1 = LinkedList()
    return list_1
