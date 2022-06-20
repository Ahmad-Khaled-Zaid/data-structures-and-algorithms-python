from Linked_List.linked_list import LinkedList


def zip_lists(list1, list2):
    current1 = list1.head
    current2 = list2.head
    while current2:
        if current1:
            list1.insert_after(current1.value, current2.value)
            current1 = current1.next.next
            current2 = current2.next
        else:
            list1.insert_last(current2.value)
            current2 = current2.next


if __name__ == '__main__':
    list_1 = LinkedList()
    list_2 = LinkedList()
    list_1.insert_last(1)
    list_1.insert_last(3)
    list_1.insert_last(2)

    list_2.insert_last(5)
    list_2.insert_last(9)
    list_2.insert_last(4)

    zip_lists(list_1, list_2)
    print(list_1.to_string())
