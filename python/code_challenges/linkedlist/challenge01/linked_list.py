from locale import currency


class LinkedList:
    """
    the purpose of this class to create singly linked list 
    have 1 attribute : head
    have 3 method : append(),delet(),printAll()

    """
    def __init__(self):
        self.head = None
    
    def __str__(self):
        return "The purpose of this class is to create a singly linked list, append a new node to it, and delete the node from it"
    
    def __repr__(self) -> str:
        return 'append or delete a node from linkedlist '

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
    def delete(self, value):
        """
        the perpose of this method to delete node from  linklist
        """
        if self.head is None:
            return "The linked list is empty"
        else:
            current = self.head
            if current.value==value:
                self.head=current.next
            else:
                while current is not None:
                    y=current.next
                    if y.value==value:
                        current.next=y.next
                        break              
                    current = current.next


    def printAll(self):
        """
        Print all node value in the linked List sequentially
        """
        if self.head is None:
            print( "The linked list is empty")
            return "The linked list is empty"
        else:
            current = self.head
            # add the value in node inside array "x" to make it easier to test
            x=[]
            while current is not None:
                x.append(current.value)
                print(current.value)
                current = current.next
            return x