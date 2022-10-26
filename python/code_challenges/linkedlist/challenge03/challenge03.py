# Write here the code challenge solution
from node import Node

class LinkedList:
    """
    the purpose of this class to create singly linked list 
    have 1 attribute : head
    have 3 method : append(),printAll(),RemoventhNode()

    """
    def __init__(self):
        self.head = None
    
    def __str__(self):
        return "The purpose of this class is to create a singly linked list, append a new node to it and Remove nth Node "
    
    def __repr__(self) -> str:
        return 'append a node from linkedlist '

    def append(self, node):
        """
        the perpose of this method to append node to the linklist
        """
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        """
        Print all node value in the linked List sequentially
        """
        if self.head is None:
            return []
        else:
            current = self.head
            # add the value in node inside array "x" to make it easier to test
            x=[]
            while current is not None:
                x.append(current.value)
                current = current.next
            return x
    def RemoventhNode(self, n: int):
        """
        the perpose of this methode to remove the nth node from the end of the linkedlist and return its head
        it takes a head  of a linked list as argument and the nth 
        return the head
        """
        current =self.head
        i=0
        while current is not None :
            i+=1
            current=current.next 
        if i==0:
            return "the linkedlist empty"
        elif i==1:
            self.head=None
        elif i==2:
            if i-n==1:
                self.head.next=None
            else:
                self.head=self.head.next        
        elif i>2:
            current=self.head        
            i-=n
            while i>0 :
                current=current.next
                i-=1
            if current.next is not None :
                next=current.next
                current.value=next.value
                current.next=next.next
                next.next=None
                next.value=None
            else:
                current=self.head
                next=self.head.next
                while next.next is not None :
                    current=current.next
                    next=next.next
                current.next =None
        return self.head





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
    print("--------------- first example ------------")
    print("-------------input linked list ------------")
    print(linkedList1.printAll())
    print("*******************************************************")

    n=int(input("*****  Enter the nth node you want to remove it  ******\n***** Not :the nth node from the end of linkedlist ****\n*******************************************************\n >"))
    #remove the nth node from the end of the linkedlist
    linkedList1.RemoventhNode(n)
    print(f"-------------- output linked list   --------------------")
    print(linkedList1.printAll())
    print ("\n################################################################################################################################\n")


    #creat the secand linkedlist nodes
    linkedList2 = LinkedList()
    node1 = Node(1)
    linkedList2.append(node1)
    
    print("--------------- secand example ------------")
    print("-------------input linked list ------------")
    print(linkedList2.printAll())
    print("*******************************************************")

    print("*********              nth = 1               **********\n*******************************************************")
    n=1
    #remove the nth node from the end of the linkedlist
    linkedList2.RemoventhNode(n)
    print("linkedList2.head.value ",linkedList2.head)
    print(f"-------------- output linked list   --------------------")
    print(linkedList2.printAll())
    print ("\n################################################################################################################################33\n")



    #creat the third linkedlist nodes

    linkedList3 = LinkedList()
    node1 = Node(1)
    linkedList3.append(node1)
    node2 = Node(2)
    linkedList3.append(node2)
    
    print("--------------- third example ------------")
    print("-------------input linked list ------------")
    print(linkedList3.printAll())
    print("*******************************************************")

    print("*********              nth = 1               **********\n*******************************************************")
    n=1
    #remove the nth node from the end of the linkedlist
    linkedList3.RemoventhNode(n)
    print(f"-------------- output linked list   --------------------")
    print(linkedList3.printAll())