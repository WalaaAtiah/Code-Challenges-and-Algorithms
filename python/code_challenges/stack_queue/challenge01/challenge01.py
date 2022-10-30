# Write here the code challenge solution
from unittest import result
from stack import Stack

#creat queue class
class MyQueue :
    '''
    this class Implement a first in first out (FIFO) queue using only two stacks. 
    have 5 method  ( __str__(),push(), peek() , pop(), and empty()).
    and have 2 attribute (stack1 ,stack_rev self.size, self.result)
    '''
    def __init__(self):
        """
        initialize method 
        """
        self.stack1=Stack()
        self.stack_rev=Stack()
        self.size=0
        self.result=[]

    def __str__(self):
        return "Implement a first in first o (FIFO) queue"

    def push (self,value):
        """
         to Pushe element value to the back of the queue.
        """
        if len(self.result)!=0 and self.stack1.top is None:
            for i in self.result:
                self.stack1.push(i)   
        self.result.append(value)
        self.stack1.push(value)
        self.size +=1

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        """
        if self.size ==0:
            return "This queue is empty"
        while not self.stack1.is_empty():
            self.stack_rev.push(self.stack1.pop())
        
        self.size -=1
        self.result.pop(0)
        return self.stack_rev.pop()

    def peek(self):
        """
        Returns the element at the front of the queue.
        """
        if self.size ==0:
            return "This queue is empty"
        while not self.stack1.is_empty():
            self.stack_rev.push(self.stack1.pop())
        return self.stack_rev.peek()

    def empty(self):
        """
         Returns true if the queue is empty, false otherwise.
        """
        return self.size == 0
    def print_as_list(self):
        return self.result


if __name__ =="__main__":
    print ("""
    Welcome to queue data structure
    """)
    # creat queue 
    queue1=MyQueue ()
    # add a new element to the queue py use push methode [1,2]
    queue1.push(1)
    print("queue is: ", queue1.print_as_list())
    queue1.push(2)
    print("queue is: ",queue1.print_as_list())
    queue1.push(3)
    print("queue is: ",queue1.print_as_list())

    print("queue1.pop() :>> ",queue1.pop())
    print("queue is: ",queue1.print_as_list())
    print("queue1.pop() :>> ",queue1.pop())

    print("queue is: ",queue1.print_as_list())

    print("queue1.peek() : >> ",queue1.peek())

    print("queue1.pop() :>> ",queue1.pop())
    queue1.push(4)
    print("queue is: ",queue1.print_as_list())
    print("queue1.pop() :>> ",queue1.pop())
   
    print("queue1.empty() :>> ",queue1.empty())