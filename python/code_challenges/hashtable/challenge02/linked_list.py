class Node:
    def __init__(self, data):
        '''
        this class to create a node  have 2 attribute (data,next)
        '''
        self.data = data
        self.next = None


class LinkedList:
    '''
        this class to create a node  have :
        1 attribute (head)
        3 methode  add() , duplicate_node() , __str__()
    '''
    def __init__(self):
        self.head = None

    def add(self, data):

        """
        this methode to add anew node to the linked list 
        input : data 
        output : None
        
        """
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

        '''
       this method to check if this value is duplicate in the linked list
        input : val 
        output : boolean (true ,false )or string if the linkedlist empty 
        '''
        if self.head ==None:
            return "the linked list empty"
        y=0
        # print([val],self.head.data)
        current=self.head
        while current:
            # print(current.data==[val])
            if current.data==[val]:
                y +=1
            current=current.next
        # print(y)
        if y>1:
            return True
        return False


    def __str__(self):
        """
        this method to loop through the linked list and print the value inside it        
        """
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'