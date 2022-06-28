from Stack_and_Queue.stack_and_queue import Stack, QueueIsEmpty


class PseudoQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.str_queue = ""

    def enqueue(self, value):
        self.stack1.push(value)

    def __str__(self):
        self.str_queue = ""
        curr = self.stack1.top
        while curr:
            self.str_queue += f"[{curr.value}]->"
            curr = curr.next
        return self.str_queue

    def dequeue(self):
        if not self.stack1.top:
            raise QueueIsEmpty

        curr = self.stack1.top
        while curr.next is not None:
            self.stack2.push(self.stack1.pop())
            curr = curr.next
        popped_value = self.stack1.pop()
        curr = self.stack2.top

        while curr:
            self.stack1.push(self.stack2.pop())
            curr = curr.next
        return popped_value


if __name__ == '__main__':
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    # queue.d


