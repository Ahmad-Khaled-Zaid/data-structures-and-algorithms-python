class Node:
    """
    | a class to represent a Node in the Linked List
    | ...
    | Attribute:
    |  ------------
    | value : the value that live inside the Node
    | next : a pointer from type Node that reference to the next Node in the Linked List
    | ------------

    | Methods:
    | ------------
    No Methods
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
        | a class to represent a Linked List
        | ...
        | Attribute:
        |  ------------
        | head : a reference to the new node in the linked list
        | current : a reference to the current node being loop over
        | text : a variable to represent the Linked list in a string form

        | ------------

        | Methods:
        | insert_first(value):
            add a new Node to the Linked List
        | includes(value)
            check if a value exists in the Linked List
        | to_string()
            print a linked list in representational form

        | ------------
        """

    def __init__(self):
        self.head = None
        self.current = None
        self.text = ""

    def insert_first(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node
        self.current = self.head

    def includes(self, value):

        self.current = self.head
        while self.current is not None:
            if value == self.current.value:
                return True
            self.current = self.current.next
        return False

    def to_string(self):
        self.current = self.head
        while self.current is not None:
            self.text += " { " + str(self.current.value) + " } -> "
            self.current = self.current.next
        self.text += "Null"
        return self.text


if __name__ == "__main__":
    try:
        list_1 = LinkedList()
        list_1.insert_first(5)
        list_1.insert_first(10)
        list_1.insert_first(52)
        list_1.insert_first(2)
        list_1.insert_first()
    except Exception as error:
        print(f"Error: {error}")