from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest


def test_enqueue_case1(queue):
    actual = queue.stack1.top.value
    expected = 5
    assert actual == expected


def test_enqueue_case2(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(5)

    actual = queue.stack1.top.value
    expected = 5
    assert actual == expected


def test_dequeue_case1(queue):
    actual = queue.dequeue()
    expected = 20
    assert actual == expected


def test_dequeue_case2(queue):
    queue.dequeue()
    actual = queue.dequeue()
    expected = 15
    assert actual == expected


@pytest.fixture
def queue():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)

    return queue
