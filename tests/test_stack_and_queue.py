import pytest
from Stack_and_Queue.stack_and_queue import Stack, StackIsEmpty, Queue, QueueIsEmpty


def test_push_onto_stack(stack):
    actual = stack.peek()
    expected = 1
    assert actual == expected


def test_push_push_multiple_values(stack):
    stack.push(2)
    stack.push(3)
    actual = stack.peek()
    expected = 3
    assert actual == expected


def test_pop_off_the_stack(stack):
    actual = stack.pop()
    expected = 1
    assert actual == expected


def test_empty_stack_after_multiple_pop(stack):
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


def test_new_peek(stack):
    stack.push(2)
    actual = stack.peek()
    expected = 2
    assert actual == expected


def test_instantiate_empty_stack():
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected


def test_calling_peek_or_pop_on_empty_stack():
    stack = Stack()
    with pytest.raises(StackIsEmpty):
        stack.peek()


def test_enqueue_into_queue(queue):
    queue.enqueue(1)
    actual = queue.peek()
    expected = 1
    assert actual == expected


def test_enqueue_multiple_values(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.rare.value
    expected = 2
    assert actual == expected


def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected


def test_peek_the_queue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.peek()
    expected = 1
    assert actual == expected


def test_empty_the_queue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected


def test_instantiate_empty_queue(queue):
    actual = queue.is_empty()
    expected = True
    assert actual == expected


def test_calling_peek_or_pop_on_empty_queue(queue):
    with pytest.raises(QueueIsEmpty):
        queue.peek()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    return stack


@pytest.fixture
def queue():
    queue = Queue()
    return queue
