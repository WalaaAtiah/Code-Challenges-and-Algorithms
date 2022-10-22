# Write your test here
import pytest 
from unittest import mock
import builtins
from node import Node
from linked_list import LinkedList


def test_delete_listedlink_empty():
    linkedList2 = LinkedList()
    actual =linkedList2.delete(4)
    expected="The linked list is empty"
    assert actual == expected


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
    expected='append or delete a node from linkedlist '
    assert actual == expected

def test_delete1(creat):
    creat.delete(4)
    actual =creat.printAll()
    expected=[5,1,9]
    assert actual == expected

def test_delete2(creat):
    creat.delete(5)
    actual =creat.printAll()
    expected=[4,1,9]
    assert actual == expected

def test_delete3(creat):
    creat.delete(1)
    actual =creat.printAll()
    expected=[4,5,9]
    assert actual == expected

def test_delete4(creat):
    creat.delete(9)
    actual =creat.printAll()
    expected=[4,5,1]
    assert actual == expected