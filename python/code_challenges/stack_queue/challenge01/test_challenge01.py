# Write your test here
from inspect import stack
import pytest
from stack import Stack
from challenge01 import MyQueue 

#test for the stack 
@pytest.fixture
def stack():
    stack1  = Stack()
    stack1.push("H")
    stack1.push("E")
    stack1.push("L")
    stack1.push("L")
    stack1.push("O")
    return stack1

def test_stack_one(stack):
    assert stack.pop()=="O"
def test_stack_two(stack):
    assert stack.get_size()==5



@pytest.fixture
def queue1():
    return  MyQueue ()



def test_queue_one(queue1):
    assert queue1.__str__()=="Implement a first in first o (FIFO) queue"

def test_queue_two(queue1):
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    assert queue1.print_as_list()==[1,2,3,4]

def test_queue_three(queue1):
    assert queue1.empty()==True

def test_queue_four(queue1):
    assert queue1.pop()=="This queue is empty"

def test_queue_five(queue1):
    assert queue1.peek()=="This queue is empty"

def test_queue_pop(queue1):
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    assert queue1.pop()==1

def test_queue_peek(queue1):
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    assert queue1.peek()==1

def test_have_Push_After_Pop(queue1):
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    queue1.pop() # delete the first item 1
    queue1.pop() # delet the secand item 2
    queue1.push(66)
    assert queue1.print_as_list()==[3, 4, 66]