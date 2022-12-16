# Write here the code challenge solution
from linked_list import LinkedList,Node

class HashTabel():
    """
    this class to create a hashtable have :
    2 attribute (size(int) , map(list))
    
    """
    def __init__(self, size=5):
        self.size = size
        self.map = [None]*size
        # self.map = [LinkedList()]*size
        # self.map = [[]]*size

    def custom_hash(self, key):
        """
        this method for create hash algorithem :
        input : key (int,string)
        output: index (int)
        
        """
        sum_of_asccii = 0
        for ch in key: #get sum for asccii codes
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*193
        indx = temp%self.size
        return indx

    def set(self, key):
        """
        this methode to set the key in the hashtable :
        input : key(int,string)
        output:None 
        """
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]: # if he buchet is empty
            self.map[hashed_key] = [key]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key])
            else: # if the bucket contains one pair only
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair = [key]
                self.map[hashed_key] = chain
                chain.add(existing_pair)
                chain.add(new_pair)
    
    def create_hashTable_from_string(self,string):
        """
        this methode to create hashTable from string:
        input :string
        output :None 
        """
        array=string.split()
        for i in array:
           self.set(i)

    def __str__ (self):
        values = ''
        for i in range(self.size):
            values+=f'{i} :{self.map[i]} \n'

        return values

def Repeated_Word(string,hashtable):
    """
    this function to searche about first repeated word in that string.
    input :string
    output :string 
    """
    x=string.split()
    hashtable.create_hashTable_from_string(string)
    for i in x:
        hashed_key = hashtable.custom_hash(i)
        
        if hashtable.map[hashed_key] and isinstance(hashtable.map[hashed_key], LinkedList) :
            # print(i,hashed_key,self.map[hashed_key].duplicate_node(i))
            if hashtable.map[hashed_key].duplicate_node(i):
                # print(i)
                return i
    # print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    return "No Repetition"
    
    





if __name__ == "__main__":

    print("##################### Example 1 #########################################")
    hashtabel1 = HashTabel()
    st="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    print ("input= ",st )

    print("Repeated Word:  " ,Repeated_Word(st,hashtabel1))
    print("\n*************************************************************************************************\n")

    print("##################### Example 2 #########################################")
    hashtabel2 = HashTabel()
    st2="I am learning programming at ASAC"
    print ("input= ",st2 )
    print("Repeated Word:  " ,Repeated_Word(st2,hashtabel2))
    print("\n*************************************************************************************************\n")

    print("##################### Example 3 #########################################")
    hashtabel3= HashTabel()
    st3=""
    print ("input= ",st3 )
    print("Repeated Word:  " ,Repeated_Word(st3,hashtabel3))
    print("\n*************************************************************************************************\n")

    print("##################### Example 4 #########################################")
    hashtabel4= HashTabel()
    st4="hi"
    print ("input= ",st4 )   
    print("Repeated Word:  " ,Repeated_Word(st4,hashtabel4))
    print("*************************************************************************************************")
