import py
import pytest
from _pytest.fixtures import fixture

from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter


def test_equeue_case1(queue):
    actual = queue.front.name
    expected = "sherry"
    assert actual == expected


def test_equeue_case2(queue):
    actual = queue.rear.name
    expected = "candy"
    assert actual == expected


def test_dequeue_case1(queue):
    actual = queue.dequeue("cat")
    expected = "sherry"
    assert actual == expected


def test_dequeue_case2(queue):
    actual = queue.dequeue("dog")
    expected = "Rex"
    assert actual == expected


def test_dequeue_case3(queue2):
    actual = queue2.dequeue("dog")
    expected = "candy"
    assert actual == expected


def test_dequeue_case4(queue2):
    actual = queue2.dequeue("dog")
    expected = "candy"
    assert actual == expected


def test_dequeue_case5(queue3):
    actual = queue3.dequeue("dog")
    expected = "slim"
    assert actual == expected


@pytest.fixture
def queue():
    queue = AnimalShelter()
    queue.enqueue("sherry", "cat")
    queue.enqueue("Alex", "cat")
    queue.enqueue("Rex", "dog")
    queue.enqueue("Sugar", "cat")
    queue.enqueue("slim", "cat")
    queue.enqueue("candy", "dog")
    return queue


@pytest.fixture
def queue2():
    queue = AnimalShelter()
    queue.enqueue("Rex", "cat")
    queue.enqueue("Sugar", "cat")
    queue.enqueue("sherry", "cat")
    queue.enqueue("Alex", "cat")
    queue.enqueue("slim", "cat")
    queue.enqueue("candy", "dog")
    return queue


@pytest.fixture
def queue3():
    queue = AnimalShelter()
    queue.enqueue("Rex", "cat")
    queue.enqueue("Sugar", "cat")
    queue.enqueue("sherry", "cat")
    queue.enqueue("slim", "dog")
    queue.enqueue("Alex", "dog")
    queue.enqueue("candy", "dog")
    return queue
