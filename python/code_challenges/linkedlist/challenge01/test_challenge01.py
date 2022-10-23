# Write your test here
import pytest 
from node import Node
from linked_list import LinkedList
from challenge01 import delete


def test_delete_listedlink_empty():
    linkedList2 = LinkedList()
    assert linkedList2.printAll() == "The linked list is empty"

def test_delete_one():
    linkedList2 = LinkedList()
    node1 = Node(4)
    linkedList2.append(node1)
    node2 = Node(5)
    linkedList2.append(node2)
    node3 = Node(1)
    linkedList2.append(node3)
    node4 = Node(9)
    linkedList2.append(node4)
    delete(node1)
    assert linkedList2.printAll() == [5,1,9]

def test_delete_two():
    linkedList2 = LinkedList()
    node1 = Node(4)
    linkedList2.append(node1)
    node2 = Node(5)
    linkedList2.append(node2)
    node3 = Node(1)
    linkedList2.append(node3)
    node4 = Node(9)
    linkedList2.append(node4)
    delete(node2)
    assert linkedList2.printAll() == [4,1,9]

def test_delete_three():
    linkedList2 = LinkedList()
    node1 = Node(4)
    linkedList2.append(node1)
    node2 = Node(5)
    linkedList2.append(node2)
    node3 = Node(1)
    linkedList2.append(node3)
    node4 = Node(9)
    linkedList2.append(node4)
    delete(node3)
    assert linkedList2.printAll() == [4,5,9]

def test_delete_four():
    linkedList2 = LinkedList()
    node1 = Node(4)
    linkedList2.append(node1)
    node2 = Node(5)
    linkedList2.append(node2)
    node3 = Node(1)
    linkedList2.append(node3)
    node4 = Node(9)
    linkedList2.append(node4)
    delete(node4)
    assert linkedList2.printAll() == [4,5,1,9]


@pytest.fixture
def creat():
    linkedList1 = LinkedList()
    node1 = Node(4)
    linkedList1.append(node1)
    node2 = Node(5)
    linkedList1.append(node2)
    node3 = Node(1)
    linkedList1.append(node3)
    node4 = Node(9)
    linkedList1.append(node4)

    return linkedList1


def test_str(creat):
    actual =creat.__str__()
    expected="The purpose of this class is to create a singly linked list, append a new node to it, and delete the node from it"
    assert actual == expected

def test_rper(creat):
    actual =creat.__repr__()
    expected='append a node from linkedlist '
    assert actual == expected

# def test_delete1():
#     delete()
#     actual =creat.printAll()
#     expected=[5,1,9]
#     assert actual == expected

# def test_delete2(creat):
#     creat.delete(5)
#     actual =creat.printAll()
#     expected=[4,1,9]
#     assert actual == expected

# def test_delete3(creat):
#     creat.delete(1)
#     actual =creat.printAll()
#     expected=[4,5,9]
#     assert actual == expected

# def test_delete4(creat):
#     creat.delete(9)
#     actual =creat.printAll()
#     expected=[4,5,1]
#     assert actual == expected