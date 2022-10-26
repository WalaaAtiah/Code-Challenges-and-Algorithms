# Write your test here
# Write your test here
import pytest 
from node import Node
from challenge03 import LinkedList

# test if the linked list empty
def test_1():
    linkedList1 = LinkedList()
    assert linkedList1.RemoventhNode(1)=="the linkedlist empty"

# # test two input :head = [1,2,3,4,5], n = 2 
def test_2():
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
    linkedList1.RemoventhNode(2)
    assert linkedList1.printAll()==[1, 2, 3, 5]

# # test three input : head = [1], n = 1
def test_3():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    linkedList1.RemoventhNode(2)
    assert linkedList1.printAll()==[]

#test four input : head = [1,2], n = 1
def test_4():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    print(linkedList1.printAll())
    linkedList1.RemoventhNode(1)
    print(linkedList1.printAll())
    assert linkedList1.printAll()==[1]

    #test five input : [1,2,3]  n=1
def test_5():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    print(linkedList1.printAll())
    linkedList1.RemoventhNode(1)
    print(linkedList1.printAll())
    assert linkedList1.printAll()==[1,2]

#test six input : [1,2,3]  n=3
def test_6():
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    print(linkedList1.printAll())
    linkedList1.RemoventhNode(3)
    print(linkedList1.printAll())
    assert linkedList1.printAll()==[2,3]