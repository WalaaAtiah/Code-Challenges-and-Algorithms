# Write here the code challenge solution
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
        # print("111111111111111111",array,ds)
        del ds[x.val]
        if len(array)>0 and list(ds.keys())[0]==x.left.val:
            #  print("555555555555",array[0:1])
             x.left=rotat(array[0:2],ds,x.left)
             del array[:2]
            #  print("22222222222222222",array)
        if len(array)>0 and x.right.val==list(ds.keys())[0]:
            x.right=rotat(array[0:2],ds,x.right)
            del array[:2]
        return x
    ds = {item: None for item in array}
    x=root
    x=Node(array.pop(0))
    # print("333333333333",array,ds)

    return rotat(array,ds,x)            


# this function to solve tha challenge 
def SameTree(p,q):

    def Breadth_first(root):    
            """
            this methode to print the Breadth_first traversal as array 
            input : self ( which is the first node in tree)
            output : array 
            
            """    
            temp=root
            if temp .val is None :
                return "the tree is empty "
            queue=[temp]
            output=[]
            while queue:
                pop_node=queue.pop(0)
                if pop_node !="null":
                    output.append(pop_node.val)
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
    x=Breadth_first(p)
    y=Breadth_first(q)
    return x==y

print("####################################################################################################################")
print ("********************         Example 1          *********************\n")
print("input : p=[1,2,3] , q=[1,2,3]")
p=Tree()
p.root=insert_breadth(p.root,[1,2,3])

q=Tree()
q.root=insert_breadth(q.root,[1,2,3])

print("output= ",SameTree(p.root,q.root))

print("####################################################################################################################")
print ("********************         Example 2          *********************\n")
print("input : p=[1,2] , q=[1,null,2]")
p=Tree()
p.root=insert_breadth(p.root,[1,"null",2])

q=Tree()
q.root=insert_breadth(q.root,[1,2,3])

print("output= ",SameTree(p.root,q.root))

print("####################################################################################################################")
print ("********************         Example 3          *********************\n")
print("input : p=[1,2] , q=[1,1,2]")
p=Tree()
p.root=insert_breadth(p.root,[1,1,2])

q=Tree()
q.root=insert_breadth(q.root,[1,2,1])

print("output= ",SameTree(p.root,q.root))
