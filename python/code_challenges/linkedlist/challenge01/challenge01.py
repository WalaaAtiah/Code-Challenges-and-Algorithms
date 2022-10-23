# Write here the code challenge solution
from node import Node
from linked_list import LinkedList

def delete(node):
        """
        the perpose of this function to delete node from  linklist
        it takes a node as argument
        the node not a tail node in the list.
        """
        if node.next==None :
            return 
        else:    
            next_node=node.next
            node.value=next_node.value
            node.next=next_node.next
     


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

    current=linkedList1.head
    while True:
        # print("insid while ")
        if current.value==v:
            print("inside if ")
            nod=current
            break
        current=current.next

    delete(nod)
    
    linkedList1.printAll()
