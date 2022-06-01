import pytest
from array_insert_shift.array_insert_shift import insert_shift_array


def test_array_1():
    actual = insert_shift_array([2, 4, 6, -8], 5)
    expected = [2, 4, 5, 6, -8]
    assert actual == expected


def test_array_2():
    actual = insert_shift_array([42, 8, 15, 23, 42], 16)
    expected = [42, 8, 15, 16, 23, 42]
    assert actual == expected


def test_array_3():
    actual = insert_shift_array([], 16)
    expected = [16]
    assert actual == expected


def test_array_4():
    actual = insert_shift_array(1, 16)
    expected = "please pass an list as a first parameter"
    assert actual == expected
