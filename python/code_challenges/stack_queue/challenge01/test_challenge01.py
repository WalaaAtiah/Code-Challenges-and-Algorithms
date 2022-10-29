# Write your test here
from inspect import stack
from stack import Stack

#test for the stack 

def test_stack():
    stack1  = Stack()
    stack1.push("H")
    stack1.push("E")
    stack1.push("L")
    stack1.push("L")
    stack1.push("O")
    assert stack1.pop()=="O"
    assert stack1.get_size()==4
    # print(stack1.pop())
    # print(stack1.pop())
    # print(stack1.pop())
    # print(stack1.peek())
    # print(stack1.get_size())