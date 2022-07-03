from trees.trees import BinaryTree, BinarySearchTree, TNode
import pytest


def test_instantiate_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_instantiate_tree_root():
    tree = BinaryTree()
    tree.root = TNode(23)
    actual = tree.root.value
    expected = 23
    assert actual == expected


def test_add_to_binary_search_tree():
    tree = BinarySearchTree()
    tree.root = TNode(23)
    tree.add(46)
    tree.add(20)
    actual1 = tree.root.right.value
    expected1 = 46
    actual2 = tree.root.left.value
    expected2 = 20
    assert actual1 == expected1
    assert actual2 == expected2


def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected


def test_in_order(tree):
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected


def test_post_order(tree):
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected


def test_contain(tree_1):
    actual = tree_1.contains(23)
    expected = True
    assert actual == expected


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = TNode("A")
    tree.root.left = TNode("B")
    tree.root.right = TNode("C")
    tree.root.left.left = TNode("D")
    tree.root.left.right = TNode("E")
    tree.root.right.left = TNode("F")
    return tree


@pytest.fixture
def tree_1():
    search_tree = BinarySearchTree()
    search_tree.root = TNode(23)
    search_tree.add(42)
    search_tree.add(8)
    search_tree.add(4)
    search_tree.add(16)
    search_tree.add(15)
    search_tree.add(22)
    search_tree.add(27)
    search_tree.add(85)
    search_tree.add(105)
    return search_tree
