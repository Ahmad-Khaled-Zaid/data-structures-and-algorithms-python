from tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinaryTree, TNode
import pytest


def test_tree_intersection(tree_i):
    actual = tree_i
    expected = ['A', 'B']
    assert actual == expected


@pytest.fixture()
def tree_i():
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

    return tree_intersection(tree1, tree2)
