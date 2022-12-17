# Write your test here
from classtree import Tree,Node
from challenge01 import Two_Sum_BST
import pytest

@pytest.fixture
def tree():
    tree=Tree()
    tree.root = Node(7)
    tree.root.left = Node(2)
    tree.root.right = Node(9)
    tree.root.right.right = Node(14)
    tree.root.left.right = Node(5)
    tree.root.left.left = Node(1) 
    return tree

def test_one(tree):
    assert Two_Sum_BST(tree.root, 3)==True

def test_two(tree):
    assert Two_Sum_BST(tree.root, 4)==False

def test_three(tree):
    tree=Tree()
    assert Two_Sum_BST(tree.root, 5)=="the tree is empty"