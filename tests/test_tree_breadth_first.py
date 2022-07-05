import pytest
from tree_breadth_first.tree_breadth_first import breadth_first
from trees.trees import BinaryTree, TNode


def test_breadth_first_case_1(tree_1):
    actual = breadth_first(tree_1)
    expected = [2, 7, 5, 2, 6, 9, 4]
    assert actual == expected


def test_breadth_first_case_2(tree_2):
    actual = breadth_first(tree_2)
    expected = [100, 12, 112, 98, 54, 500, 22]
    assert actual == expected


def test_breadth_first_case_3():
    with pytest.raises(Exception):
        breadth_first(5)


@pytest.fixture
def tree_1():
    tree = BinaryTree()
    tree.root = TNode(2)
    tree.root.left = TNode(7)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(6)
    tree.root.right.left = TNode(9)
    tree.root.right.left.left = TNode(4)
    return tree.root


@pytest.fixture
def tree_2():
    tree = BinaryTree()
    tree.root = TNode(100)
    tree.root.left = TNode(12)
    tree.root.right = TNode(112)
    tree.root.left.left = TNode(98)
    tree.root.left.right = TNode(54)
    tree.root.right.left = TNode(500)
    tree.root.right.left.left = TNode(22)
    return tree.root
