# Write here the code challenge solution
from classtree import Tree,Node
def Two_Sum_BST(root,x:int):
    if not root :
        return "the tree is empty"
    

    def check(root,x,setvalue):
        if not root:
            return False
        if x - root.val in setvalue:
            return True
        setvalue.add(root.val)
        return check(root.left,x,setvalue) or check(root.right,x,setvalue)
                
    temp=root
    setvalue=set()
    return check(temp,x,setvalue) 
        


if __name__ =='__main__':
    tree=Tree()
    tree.root = Node(7)
    tree.root.left = Node(2)
    tree.root.right = Node(9)
    tree.root.right.right = Node(14)
    tree.root.left.right = Node(5)
    tree.root.left.left = Node(1) 

    print('\n**********************************     Example 1     ************************************************\n')
    print('############### root = [7,2,9,1,5,null,14] ##################################')
  
    print("if x = 3 ",Two_Sum_BST(tree.root, 3))
    print('if x = 5 ',Two_Sum_BST(tree.root, 4))
    print('if x = 10 ',Two_Sum_BST(tree.root, 10))


    print('\n**********************************     Example 2     ************************************************\n')
    tree2=Tree()
    
    print('############### root = [] ##################################')
  
    print("if x = 3 ",Two_Sum_BST(tree2.root, 3))
