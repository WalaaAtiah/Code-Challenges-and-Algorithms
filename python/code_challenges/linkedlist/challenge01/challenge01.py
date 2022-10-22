# Write here the code challenge solution
from node import Node
from linked_list import LinkedList

if __name__ == "__main__":
    # creat the linkedlist nodes
    linkedList1 = LinkedList()
    node1 = Node(4)
    linkedList1.append(node1)

    node2 = Node(5)
    linkedList1.append(node2)

    node3 = Node(1)
    linkedList1.append(node3)

    node4 = Node(9)
    linkedList1.append(node4)

    print("-------------------- befor ----------------")
    linkedList1.printAll()
    #delete node from the linkesd list

    v=int(input("Enter the value you want to delete\n"))
    print("-------------------- after ----------------")

    linkedList1.delete(v)
    
    linkedList1.printAll()
