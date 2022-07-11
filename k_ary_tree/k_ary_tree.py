from Stack_and_Queue.stack_and_queue import Queue
from trees.trees import TNode
from copy import deepcopy


class KArrTree:
    def __init__(self):
        self.root = None


class KTNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def fizz_buzz(node):
    if node.value % 3 == 0 and node.value % 5 == 0:
        return "FizzBuzz"
    elif node.value % 3 == 0:
        return "Fizz"
    elif node.value % 5 == 0:
        return "Buzz"
    else:
        return str(node.value)


def fizz_buzz_tree(root):
    if not isinstance(root, KTNode):
        raise Exception

    new_root = deepcopy(root)
    new_tree = new_root
    new_node = fizz_buzz(new_root)
    new_root.value = new_node
    queue = Queue()
    queue.enqueue(new_root)
    while not queue.is_empty():
        new_root = queue.dequeue()
        for i in new_root.children:
            queue.enqueue(i)
            i.value = fizz_buzz(i)
    return new_tree


if __name__ == "__main__":
    k_tree = KArrTree()

    # create the root
    k_tree.root = KTNode(1)

    # the root children
    k_tree.root.children.append(KTNode(2))
    k_tree.root.children.append(KTNode(3))
    k_tree.root.children.append(KTNode(4))
    k_tree.root.children.append(KTNode(5))
    k_tree.root.children.append(KTNode(6))

    # first child children
    k_tree.root.children[0].children.append(KTNode(7))
    k_tree.root.children[0].children.append(KTNode(8))
    k_tree.root.children[0].children.append(KTNode(9))

    # second child children
    k_tree.root.children[1].children.append(KTNode(10))
    k_tree.root.children[1].children.append(KTNode(11))
    k_tree.root.children[1].children.append(KTNode(12))

    # third child children
    k_tree.root.children[2].children.append(KTNode(13))
    k_tree.root.children[2].children.append(KTNode(14))
    k_tree.root.children[2].children.append(KTNode(15))

    print(fizz_buzz_tree(k_tree.root).value)
