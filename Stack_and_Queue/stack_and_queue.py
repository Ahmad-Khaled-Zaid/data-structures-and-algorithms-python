class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackIsEmpty(Exception):
    pass


class QueueIsEmpty(Exception):
    pass


class Stack:
    def __init__(self):
        self.top = None

    def show_stack(self):
        curr = self.top
        while curr:
            print(curr.value)
            curr = curr.next

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):

        if self.is_empty():
            raise StackIsEmpty("the Stack is empty")
        else:
            temp = self.top.value
            self.top = self.top.next
            return temp

    def peek(self):
        if self.is_empty():
            raise StackIsEmpty("the Stack is empty")
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.rare = node
            self.front = self.rare
        else:
            self.rare.next = node
            self.rare = node

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmpty("the queue is empty")
        temp = self.front.value
        self.front = self.front.next
        return temp

    def is_empty(self):
        return self.front is None

    def peek(self):
        if not self.front:
            raise QueueIsEmpty("the queue is empty")
        return self.front.value


if __name__ == "__main__":
    queue = Queue()
    # queue.enqueue(4)
    # queue.enqueue(5)
    # queue.enqueue(6)
    queue.peek()
    print(queue.is_empty())
    # print(queue.peek())
