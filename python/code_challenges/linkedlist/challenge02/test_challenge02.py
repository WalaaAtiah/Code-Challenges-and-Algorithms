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
def test_MiddlenNode_2():
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
    assert MiddlenNode(linkedList1.head).value==4

# test if the number of node inside linked list is odd
def test_MiddlenNode_3():
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
    assert MiddlenNode(linkedList1.head).value==3