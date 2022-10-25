# Write here the code challenge solution
import math
from node import Node
from linked_list import LinkedList

def MiddlenNode(head):
        """
        the perpose of this function to return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.
        it takes a head as argument
        return the middel node
        """
        current=head
        count=0
        while True:
            if current==None:
                break
            else:
                count+=1
            current=current.next
        
        if count<1 or count>100:
            return "the number of node inside linked List is less than one or more than 100" 
        x=math.floor(count/2)
        c=0
        current=head
        while c!=x:
            c+=1
            current=current.next
        return current
        

    

if __name__ == "__main__":
    # creat the first linkedlist nodes
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
    print("--------------- first example ------------")
    print("-------------input linked list ------------")
    print(linkedList1.printAll())
    #find the middle node in the linkesd list
    mid=MiddlenNode(linkedList1.head)
    print(f"-------------- middle node is {mid.value}  ------------")
    print(f"-------------- output  --------------------")
    linkedList1.middel_node(mid)

    #creat the secand linkedlist nodes
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
    print("--------------- second example ------------")
    print("-------------input linked list -------------")
    print(linkedList2.printAll())
    #find the middle node in the linkesd list

    mid_node = MiddlenNode(linkedList2.head)
    print(f"-------------- middle node is {mid_node.value}  ------------")
    print(f"-------------- output  --------------------")
    linkedList2.middel_node(mid_node)