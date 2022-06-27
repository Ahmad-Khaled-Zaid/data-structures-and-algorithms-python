import math


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
        self.last_node_pointer = None
        self.length = 0

    "##################################################"
    "Method To Insert Node with O(1) Time Performance"
    "##################################################"

    def insert_first(self, value):
        self.length += 1
        node = Node(value)
        if self.length == 1:
            self.last_node_pointer = node
        node.next = self.head
        self.head = node

    "######################################################"
    "Method To Check if A Node Is Exist In the Linked List"
    "######################################################"

    def includes(self, value):
        self.current = self.head
        while self.current is not None:
            if value == self.current.value:
                return True
            self.current = self.current.next

        return False

    "######################################################"
    "Method To Insert Node at The Last Of the Linked List"
    "######################################################"

    def insert_last(self, value):
        self.length += 1

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    "#################################################################"
    "Method To Insert Node Before a Specific Node in the Linked List"
    "#################################################################"

    def insert_before(self, node_value, new_value):
        if self.head is None:
            print("You Can't Insert In Empty List")
        elif node_value == self.head.value:
            self.insert_first(new_value)
            # self.head = Node(new_value)
        else:
            self.length += 1
            node = Node(new_value)
            self.current = self.head
            while self.current is not None:
                if self.current.next is not None and self.current.next.value == node_value:
                    node.next = self.current.next
                    self.current.next = node
                    return

                self.current = self.current.next
            raise Exception

    "#################################################################"
    "Method To Insert Node After a Specific Node in the Linked List"
    "#################################################################"

    def insert_after(self, node_value, new_value):
        if self.head is None:
            print("You Can't Insert In Empty List")

        else:
            self.length += 1
            self.current = self.head
            while self.current is not None:
                if self.current.value == node_value:
                    node = Node(new_value)
                    node.next = self.current.next
                    self.current.next = node
                    return
                self.current = self.current.next
            raise Exception

    "#################################################################"
    "Method To Add Node In The Middle Of The Linked List"
    "#################################################################"

    def insert_in_middle(self, value):
        if self.head is None:
            return "You Can't Insert In Empty List"
        # elif self.length == 1:
        #     self.insert_last(value)

        else:
            counter = 0
            self.current = self.head
            while self.current is not None:
                counter += 1
                if counter == math.ceil(self.length / 2):
                    self.length += 1
                    node = Node(value)
                    node.next = self.current.next
                    self.current.next = node
                    return
                self.current = self.current.next

    "######################################################################################"
    "Method To Return the node’s value that is k places from the tail of the linked list."
    "######################################################################################"

    def kth_from_end(self, place_value):

        counter = 0
        self.current = self.head
        while self.current is not None:
            if counter == self.length - (place_value + 1):
                return self.current.value
            self.current = self.current.next
            counter += 1
        raise Exception

    "#################################################################"
    "Method To Print All The Linked List Values In A string Form"
    "#################################################################"

    def to_string(self):
        self.text = ""
        self.current = self.head
        while self.current is not None:
            self.text += " { " + str(self.current.value) + " } ->"
            self.current = self.current.next
        return self.text + " Null"


if __name__ == "__main__":
    list_1 = LinkedList()
    list_2 = LinkedList()
    # list_1

    list_1.insert_last(5)
    list_1.insert_last(108)
    list_1.insert_last(200)
    # list_2

    list_2.insert_last(1)
    list_2.insert_last(2)
    list_2.insert_last(4)
    list_2.insert_last(-1)
    list_2.insert_last(332)
    print(list_1.to_string())
    print(list_2.to_string())


# def merge_linked_lists(a, b):
#     if not a or b andaa a.value > b.value:
#         a, b = b, a
#     if a:
#         a.next = merge_linked_lists(a.next, b)
#     return a
#

# curr1 = list_1.head
# curr2 = list_2.head
# if not curr2:
#     return list_1
# if not curr1:
#     return list_2
# flag = False
# while curr2:
#     if curr2 and curr1.next is None:
#         pass
#         # if curr1.value > curr2.value:
#         #     curr2.next = curr1
#         #     return list_2
#         # else:
#         #     curr1.next = curr2
#         #     return list_1
#     elif curr1.value <= curr2.value <= curr1.next.value:
#         temp = curr2.next
#         curr2.next = curr1.next
#         curr1.next = curr2
#         curr2 = temp
#         curr1 = curr1.next
#
#     elif curr2.value < curr1.value:
#         print("hello")
#         flag = True
#         temp = curr2.next
#         curr2.next = curr1
#         curr1 = curr2
#         curr2 = temp
#     else:
#         curr1 = curr1.next
#
# if flag:
#     return list_2
# else:
#     return list_1


merge_linked_lists(list_1.head, list_2.head)
print(list_2.to_string())
#
# def sort_linked_list(linked_list_1):
#     link_list_2 = linked_list_1.head
#     curr = link_list_2
#     flag = False
#     if not curr:
#         raise Exception
#
#     if curr.next is None:
#         return linked_list_1
#
#         # 1 2 3 5 7
#     while curr.next:
#         if curr.value > curr.next.value:
#             flag = True
#             curr.value, curr.next.value = curr.next.value, curr.value
#
#         curr = curr.next
#
#         if flag and curr.next is None:
#             curr = linked_list_1.head
#             flag = False
#
#
# sort_linked_list(list_1)
# print(list_1.to_string())
