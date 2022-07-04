from trees.trees import BinaryTree, TNode
import pytest

def test_max_case1():
    tree = BinaryTree()
    tree.root = TNode(5)
    tree.root.right = TNode(10)
    tree.root.left = TNode(7)
    tree.root.right.left = TNode(19)
    tree.root.right.right = TNode(1)
    tree.root.left.right = TNode(19)
    tree.root.left.right = TNode(22)
    actual = tree.max_tree()
    expected = 22
    assert actual == expected


def test_max_case2():
    tree = BinaryTree()
    tree.root = TNode(-3)
    tree.root.right = TNode(0)
    tree.root.left = TNode(43)
    tree.root.right.left = TNode(90)
    tree.root.right.right = TNode(13)
    tree.root.left.right = TNode(25)
    tree.root.left.right = TNode(-23)
    actual = tree.max_tree()
    expected = 90
    assert actual == expected
