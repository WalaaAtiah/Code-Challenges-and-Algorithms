# Write here the code challenge solution
from unittest import result
from stack import Stack

#creat queue class
class Queue:
    '''
    this class Implement a first in first out (FIFO) queue using only two stacks. 
    have 5 method  ( __str__(),push(), peek() , pop(), and empty()).
    and have 2 attribute (stack1 ,stack_rev)
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
        self.result.append(value)
        self.stack1.push(value)
        self.size +=1
        return self.result

    def pop(self):
        while not self.stack1.is_empty():
            self.stack_rev.push(self.stack1.pop())
        self.size -=1
        return self.stack_rev.pop()
    def peek(self):
        while not self.stack1.is_empty():
            self.stack_rev.push(self.stack1.pop())
        return self.stack_rev.peek()
    def empty(self):
        return self.size == 0


if __name__ =="__main__":
    print ("""
    Welcome to queue data structure
    """)
    # creat queue 
    queue1=Queue()
    # add a new element to the queue py use push methode [1,2]
    print("queue is: ", queue1.push(1))
    print("queue is: ",queue1.push(2))

    print("queue1.peek() : >> ",queue1.peek())

    print("queue1.pop() :>> ",queue1.pop())
    print("queue1.empty() :>> ",queue1.empty())