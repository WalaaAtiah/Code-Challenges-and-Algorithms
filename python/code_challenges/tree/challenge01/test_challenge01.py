# Write your test here

import pytest
from challenge01 import Node

def test_one():
    tree=Node()
    preorder1 = [-1]
    inorder1 = [-1]
    tree.insert(preorder1,inorder1)
    assert tree.Breadth_first()==[-1]

def test_two():
    tree=Node()
    preorder1 = [3,9,20,15,7]
    inorder1 = [9,3,15,20,7]
    tree.insert(preorder1,inorder1)
    assert tree.Breadth_first()==[3, 9, 20, 15, 7]

def test_three():
    tree=Node()
    preorder = [1,2,4,8,9,10,11,5,3,6,7]
    inorder = [8,4,10,9,11,2,5,1,6,3,7]
    tree.insert(preorder,inorder)
    assert tree.Breadth_first()==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def test_four():
    tree=Node()
    preorder = []
    inorder = []
    tree.insert(preorder,inorder)
    assert tree.Breadth_first()=="the tree is empty "
