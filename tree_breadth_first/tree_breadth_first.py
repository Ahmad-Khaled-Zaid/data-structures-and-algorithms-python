from Stack_and_Queue.stack_and_queue import Queue
from trees.trees import BinaryTree, TNode


def breadth_first(root):
    if not isinstance(root, TNode):
        raise Exception
    queue = Queue()
    queue.enqueue(root)
    arr = []
    while not queue.is_empty():
        front = queue.dequeue()
        arr.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
    return arr


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = TNode(2)
    tree.root.left = TNode(7)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(6)
    tree.root.right.left = TNode(9)
    tree.root.right.left.left = TNode(4)
    print(breadth_first(tree.root))
