from inspect import stack
from stack import Stack

stack1  = Stack()
stack1.push("H")
stack1.push("E")
stack1.push("L")
stack1.push("L")
stack1.push("O")

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.peek())
print(stack1.get_size())
