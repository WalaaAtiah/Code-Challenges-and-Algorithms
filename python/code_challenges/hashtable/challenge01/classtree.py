class Node:
    """
    this class to create the Node which have 3 attributes : val,right,left 
    input : val -- int or str
    """
    def __init__(self,val=None):
        self.val=val
        self.right=None
        self.left=None
 
class Tree:
    """
    this class to create the tree which have 1 attributes : root "the first node in the tree"
    input : val -- int or str
    """
    def __init__(self):
        self.root=None

def insert_breadth(root,array):
    """
    this function to insert the node in the tree it take 2 argument the root of the tree and the breadth-first-traversal array and return the tree.root.
    input : tree.root -- Node , list --- array 
    output : tree.root
    """
    def rotat(array,ds,x):
        if len(array)>0 :
            x.left=Node(array.pop(0))
            ds[x.left.val]=x.left
        if len(array)>0 :
            x.right=Node(array.pop(0))
            ds[x.left.val]=x.left
        del ds[x.val]
        if len(array)>0 and list(ds.keys())[0]==x.left.val:
             x.left=rotat(array[0:2],ds,x.left)
             del array[:2]
        if len(array)>0 and x.right.val==list(ds.keys())[0]:
            x.right=rotat(array[0:2],ds,x.right)
            del array[:2]
        return x
    ds = {item: None for item in array}
    x=root
    x=Node(array.pop(0))

    return rotat(array,ds,x)            



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
