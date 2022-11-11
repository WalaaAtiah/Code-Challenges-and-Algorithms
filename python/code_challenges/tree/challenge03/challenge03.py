# Write here the code challenge solution
class Node:
    """
    this class to create Node have 
    3 attribute : value ,left ,right 
    """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """
    this class to create Tree have 
    1 attribute : root
    """
    def __init__(self):
        self.root = None

   





def convert_height_balanced(array):
    """
    this function to convert the Given integer array nums to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

    input : array 
    output : tree.root 
    """
    def binary(list,root):
        """
        this function to creat binary search tree by given the root and list 
        input : tree.root ---Node , list --- array
        output : tree.root --- Node
        """
        if root is None :
            root=Node(list.pop(0))
    # print(root.value)
        while list:
            if list[0] > root.value :
                if root.right is None:
                    root.right=Node(list.pop(0))
                else:
                    binary ([list.pop(0)],root.right)
    
            else :
                if root.left is None:
                    root.left=Node(list.pop(0))
                else:
                    binary ([list.pop(0)],root.left)
        
        return root
    if array == [] :
        tree=Tree()
        print("kkkkkkkkkkkkkkkkkkkk")
        return tree.root
    array.sort(reverse=True)
    print ("ggggggggg",array)
    l=len(array)//2 
    tree=Tree()
    tree.root=Node(array.pop(l))
    print(tree.root.value,array)
    return binary(array,tree.root)
 

def in_order(root,x=[]):
    """
     In order traversal function given the root of tree and return a list 
     input : tree.root
     output: list 
    """
    if root.left is not None:
        in_order(root.left,x)
    if root is not None:
        x.append(root.value)
    if root.right is not None:
        in_order(root.right,x)
    return x

def Breadth_first(root):    
        """
        this function to print the Breadth_first traversal as list 
        input : root ( which is the first node in tree)
        output : list 
        
        """    
        temp=root
        if temp .value is None :
            return "the tree is empty "
        queue=[temp]
        output=[]
        while queue:
            pop_node=queue.pop(0)
            if pop_node !="null":
                output.append(pop_node.value)
            else:
                output.append(pop_node)

            if pop_node != "null" and pop_node.left is not None :
                queue.append(pop_node.left)
                if pop_node.right is None:
                    queue.append("null")

            if pop_node != "null" and pop_node.right is not None:
                if pop_node.left is None:
                    queue.append("null")
                queue.append(pop_node.right)
        return output

def pre_order(root,x=[]):
        """
        this function to print the pre_order traversal as list 
        input : root ( which is the first node in tree) , empty list
        output : list 

        """

        if root.value is not None:
            x.append(root.value)
            # print(self.value)
        if root.left is not None:
           pre_order(root.left,x)
           if root.right is None:
            x.append("null")

        if root.right is not None:
            if root.left is None:
                x.append("null")
            pre_order(root.right,x)
        return x


# run the code 
if __name__ =="__main__":
    print("##########################################################################################\n")
    print("********************************* Example 1 **********************************************")
    nums = [0,-3,-10,5,9]
    print(f" input --- num = {nums} \n")
    tree=Tree()
    tree.root=convert_height_balanced(nums)
    # print(tree.root.value,tree.root.left.value,tree.root.right.value,tree.root.left.right.value,tree.root.right.right.value)
    print("pre_order traversal",pre_order(tree.root,[]))
    print("the In order traversal for the tree is ",in_order(tree.root))
    print("Breadth_first traversal",Breadth_first(tree.root))

    print("##########################################################################################\n")
    print("********************************* Example 2 **********************************************")
    nums = [3,1]
    print(f" input --- num = {nums} \n")
    tree=Tree()
    tree.root=convert_height_balanced(nums)
    print("pre_order traversal",pre_order(tree.root,[]))
    print("the In order traversal for the tree is ",in_order(tree.root,[]))
    print("Breadth_first traversal",Breadth_first(tree.root))

    print("##########################################################################################\n")
    print("********************************* Example 3 **********************************************")
    nums = [3]
    print(f" input --- num = {nums} \n")
    tree=Tree()
    tree.root=convert_height_balanced(nums)
    print("pre_order traversal)",pre_order(tree.root,[]))
    print("the In order traversal for the tree is ",in_order(tree.root,[]))
    print("Breadth_first traversal",Breadth_first(tree.root))

    