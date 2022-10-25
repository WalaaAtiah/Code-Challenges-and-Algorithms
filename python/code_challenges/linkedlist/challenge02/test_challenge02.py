# Write your test here
import pytest 
from node import Node
from linked_list import LinkedList
from challenge02 import MiddlenNode

# test if the linked list empty
def test_MiddlenNode_1():
    linkedList1 = LinkedList()
    assert MiddlenNode(linkedList1.head)=="the number of node inside linked List is less than one or more than 100"

# test if the number of node inside linked list is even
@pytest.fixture
def linkedList1():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    node4 = Node(4)
    linkedList1.append(node4)
    node5 = Node(5)
    linkedList1.append(node5)
    node6 = Node(6)
    linkedList1.append(node6)
    return linkedList1

def test_MiddlenNode_2(linkedList1):
    assert MiddlenNode(linkedList1.head).value==4

def test_MiddlenNode_3(linkedList1):
    mid=MiddlenNode(linkedList1.head)
    assert linkedList1.middel_node(mid)==[4, 5, 6]






# test if the number of node inside linked list is odd
@pytest.fixture
def linkedList2():
    linkedList2 = LinkedList()
    node1 = Node(1)
    linkedList2.append(node1)
    node2 = Node(2)
    linkedList2.append(node2)
    node3 = Node(3)
    linkedList2.append(node3)
    node4 = Node(4)
    linkedList2.append(node4)
    node5 = Node(5)
    linkedList2.append(node5)
    return linkedList2

def test_MiddlenNode_4(linkedList2):
    assert MiddlenNode(linkedList2.head).value==3

def test_MiddlenNode_5(linkedList2):
    mid=MiddlenNode(linkedList2.head)
    assert linkedList2.middel_node(mid)==[3, 4, 5]

