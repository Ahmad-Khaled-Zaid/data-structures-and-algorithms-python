import pytest
from Linked_List.linked_list import LinkedList
from zip_list.zip_list import zip_lists


def test_case1(lists):
    lists[0].insert_last(2)
    lists[1].insert_last(4)
    zip_lists(lists[0], lists[1])
    actual = lists[0].to_string()
    expected = " { 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> Null"
    assert actual == expected


def test_case2(lists):
    lists[1].insert_last(4)
    zip_lists(lists[0], lists[1])
    actual = lists[0].to_string()
    expected = " { 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> Null"
    assert actual == expected


def test_case3(lists):
    lists[0].insert_last(2)
    zip_lists(lists[0], lists[1])
    actual = lists[0].to_string()
    expected = " { 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> Null"
    assert actual == expected


@pytest.fixture
def lists():
    list_1 = LinkedList()
    list_2 = LinkedList()
    list_1.insert_last(1)
    list_1.insert_last(3)
    list_2.insert_last(5)
    list_2.insert_last(9)
    return list_1, list_2
