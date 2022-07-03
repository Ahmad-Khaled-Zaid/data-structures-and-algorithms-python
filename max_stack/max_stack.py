

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackIsEmpty(Exception):
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

    def max_stack(self):
        max_value = stack.pop()

        while not self.is_empty():
            compared_value = stack.pop()
            if compared_value > max_value:
                max_value = compared_value

        return max_value


if __name__ == "__main__":
    stack = Stack()
    stack.push(1.5)
    stack.push(45.6)
    stack.push(40)
    print(stack.max_stack())
