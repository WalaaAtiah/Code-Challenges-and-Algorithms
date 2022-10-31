# Write here the code challenge solution
def isValid(s: str) -> bool:
    """
    this function determin if the input string is valid or not :
    the input string s containing a characters '(', ')', '{', '}', '[' and ']'
    
    * An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    input : s : string
    output :boolean 
    """
    if len(s)==0:
        return "the string is empty"
    stack=[]
    dect={"[":"]" ,"(":")","{":"}"}
    for i in range(len(s)):
        if s[i] in dect:
            stack.append(s[i])
        elif s[i] in dect.values():
            if len(stack)==0:
                return False
            key =list({x for x in dect if dect[x]==s[i]})
            if stack[len(stack)-1] == key[0]:
                stack.pop()
            else:
                return False
    return not stack 


if __name__ =="__main__":
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("[({}]"))
    print(isValid("[(hello)()]"))
    print(isValid("[{(())}]"))
    print(isValid(""))