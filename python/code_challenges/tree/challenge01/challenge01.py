# Write here the code challenge solution
class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, preorder,inorder):
        """
        this method to create a tree depend to the preorder,inorder list:
        input :Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
        output :return the binary tree (self object) which have the first node in the tree
        """
        if len(preorder) ==0:
            return "the tree is empty"
        self.value=preorder[0]
        ind=inorder.index(preorder[0])
        if len(preorder) ==1:
            return self
        # print(ind)
        liftpre=preorder[1:ind+1]
        # print("liftpre",liftpre)
        liftin=inorder[0:ind]
        # print("liftin",liftin)
        rightpre=preorder[ind+1:]
        # print("rightpre",rightpre)
        rightin=inorder[ind+1:]
        # print("rightin",rightin)

        if len(liftin) ==1:
            self.left=Node(liftin[0])
        else:
            self.left=Node()
            self.left.insert(liftpre,liftin)
        if len(rightin)==1:
            self.right=Node(rightin[0])
        else:
            self.right=Node()
            self.right.insert(rightpre,rightin)
        return self
    


    def Breadth_first(self):    
        """
        this methode to print the Breadth_first traversal as list 
        input : self ( which is the first node in tree)
        output : list 
        
        """    
        temp=self
        if temp .value is None :
            return "the tree is empty "
        queue=[temp]
        output=[]
        while queue:
            pop_node=queue.pop(0)
            output.append(pop_node.value)

            if pop_node.left is not None :
                queue.append(pop_node.left)

            if pop_node.right is not None:
                queue.append(pop_node.right)
        return output


    def pre_order(self,x=[]):
        """
        this methode to print the pre_order traversal as list 
        input : self ( which is the first node in tree) , empty list
        output : list 

        """
        if self.value is not None:
            x.append(self.value)
            # print(self.value)
        if self.left is not None:
            self.left.pre_order(x)
        if self.right is not None:
            self.right.pre_order(x)
        return x

    def in_order(self,x=[]):
        """
        input : self ( which is the first node in tree) , empty list
        output : list 

        """
        if self.left is not None:
            self.left.in_order(x)
        if self is not None:
            # print(self.value)
            x.append(self.value)
        if self.right is not None:
            self.right.in_order(x)
        return x

print("####################################################################################################################")
print ("********************         Example 1          *********************\n")
preorder = [1,2,4,8,9,10,11,5,3,6,7]
inorder = [8,4,10,9,11,2,5,1,6,3,7]
print (f"input : preorder = {preorder} and the inorder = {inorder}")
tree=Node()
tree.insert(preorder,inorder)
print("-----------------------------------------------------------------------------------------------------------------\n")

print("after creat tree the output for: ")
print("output preorder",tree.pre_order())
print("-----------------------------------------------------")
print("output inorder",tree.in_order())
print("-----------------------------------------------------")
print("ouput breadth first",tree.Breadth_first())

print("####################################################################################################################\n")
print ("********************         Example 2          *********************\n")
preorder1 = [3,9,20,15,7]
inorder1 = [9,3,15,20,7]
print (f"input : preorder = {preorder1} and the inorder = {inorder1}")
tree1=Node()
tree1.insert(preorder1,inorder1)
print("-----------------------------------------------------------------------------------------------------------------\n")
x=[]
y=[]
print("after creat tree the traversal for: ")
print("preorder traversal",tree1.pre_order(x))
print("-----------------------------------------------------")
print("inorder traversal",tree1.in_order(y))
print("-----------------------------------------------------")
print("ouput  breadth first",tree1.Breadth_first())


print("####################################################################################################################\n")
print ("********************         Example 3          *********************\n")
preorder1 = [-1]
inorder1 = [-1]
print (f"input : preorder = {preorder1} and the inorder = {inorder1}")
tree1=Node()
tree1.insert(preorder1,inorder1)
print("-----------------------------------------------------------------------------------------------------------------\n")
x=[]
y=[]
print("after creat tree the traversal for: ")
print("preorder traversal",tree1.pre_order(x))
print("-----------------------------------------------------")
print("inorder traversal",tree1.in_order(y))
print("-----------------------------------------------------")
print("ouput  breadth first",tree1.Breadth_first())