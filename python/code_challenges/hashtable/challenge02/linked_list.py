class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def duplicate_node(self,val):
        if self.head ==None:
            return "the linked list empty"
        y=0
        print(val,self.head.data)
        current=self.head
        while current:
            print(current.data==[val])
            if current.data==val:
                y +=1
            current=current.next
        print(y)
        if y>1:
            return True
        return False


    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'