# Write here the code challenge solution
# import math
# from node import Node
# from challenge03 import LinkedList

# def RemoventhNode(head, n: int):
#         """
#         the perpose of this function to remove the nth node from the end of the linkedlist and return its head
#         it takes a head  of a linked list as argument and the nth 
#         return the head
#         """
#         current =head
#         i=0
#         while current is not None :
#             i+=1
#             current=current.next 
#         print('head inside remove function',head)
#         if i==0:
#             return "the linkedlist empty"
#         elif i==1:
#             head=None
#         elif i==2:
#             if i-n==1:
#                 head.next=None
#             else:
#                 head=head.next        
#         elif i>2:
#             current=head        
#             i-=n
#             while i>0 :
#                 current=current.next
#                 i-=1
#             if current.next is not None :
#                 next=current.next
#                 current.value=next.value
#                 current.next=next.next
#                 next.next=None
#                 next.value=None
#             else:
#                 current=head
#                 next=head.next
#                 while next.next is not None :
#                     current=current.next
#                     next=next.next
#                 current.next =None
#         print ('the end of remove function',head)
#         return head
        

    

# if __name__ == "__main__":
#     # creat the first linkedlist nodes
#     linkedList1 = LinkedList()
#     node1 = Node(1)
#     linkedList1.append(node1)

#     node2 = Node(2)
#     linkedList1.append(node2)

#     node3 = Node(3)
#     linkedList1.append(node3)

#     node4 = Node(4)
#     linkedList1.append(node4)

#     node5 = Node(5)
#     linkedList1.append(node5)
#     print("--------------- first example ------------")
#     print("-------------input linked list ------------")
#     print(linkedList1.printAll())
#     print("*******************************************************")

#     n=int(input("*****  Enter the nth node you want to remove it  ******\n***** Not :the nth node from the end of linkedlist ****\n*******************************************************\n >"))
#     #remove the nth node from the end of the linkedlist
#     RemoventhNode(linkedList1.head,n)
#     print(f"-------------- output linked list   --------------------")
#     print(linkedList1.printAll())


#     #creat the secand linkedlist nodes
#     linkedList2 = LinkedList()
#     node1 = Node(1)
#     linkedList2.append(node1)
#     node2 = Node(2)
#     linkedList2.append(node2)

#     print("--------------- secand example ------------")
#     print("-------------input linked list ------------")
#     print(linkedList2.printAll())
#     print("*******************************************************")

#     print("*********              nth = 1                **********\n*******************************************************")
#     n=2
#     #remove the nth node from the end of the linkedlist
#     linkedList2.head= RemoventhNode(linkedList2.head,n)
#     print("linkedList2.head.value ",linkedList2.head)
#     print(f"-------------- output linked list   --------------------")
#     print(linkedList2.printAll())

    