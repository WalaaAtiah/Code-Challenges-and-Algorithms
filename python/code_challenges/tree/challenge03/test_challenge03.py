# Write your test here
from challenge03 import convert_height_balanced,Tree,Breadth_first
def test_one():
    tree=Tree()
    tree.root=convert_height_balanced([0,-3,-10,5,9])
    assert Breadth_first(tree.root) == [0, -3, 9, -10, 'null', 5, 'null']

def test_two():
    tree=Tree()
    tree.root=convert_height_balanced([3,1])
    assert Breadth_first(tree.root) == [1, 'null', 3]

def test_three():
    tree=Tree()
    tree.root=convert_height_balanced([3])
    assert Breadth_first(tree.root) == [3]

