from trees.trees import BinaryTree, TNode
from hash_table.hash_table import HashTable


def tree_intersection(tree1, tree2):
    tree1 = tree1.pre_order()
    tree2 = tree2.pre_order()

    hashed = HashTable()
    repeat = []

    for node in tree1:
        hashed.set(node, node)

    for node in tree2:

        if hashed.contains(node):
            repeat.append(node)
        hashed.set(node, node)

    if len(repeat) == 0:
        return "theres no repeat"

    return repeat


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = TNode("A")
    tree1.root.left = TNode("B")
    tree1.root.right = TNode("C")
    tree1.root.left.left = TNode("D")
    tree1.root.left.right = TNode("E")
    tree1.root.right.left = TNode("F")

    tree2 = BinaryTree()
    tree2.root = TNode("A")
    tree2.root.left = TNode("B")
    tree2.root.right = TNode("k")
    tree2.root.left.left = TNode("r")
    tree2.root.left.right = TNode("x")
    tree2.root.right.left = TNode("m")

    print(tree_intersection(tree1, tree2))

