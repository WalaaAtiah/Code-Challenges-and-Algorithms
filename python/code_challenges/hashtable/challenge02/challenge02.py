# Write here the code challenge solution
from linked_list import LinkedList,Node

class HashTabel():
    def __init__(self, size=5):
        self.size = size
        self.map = [None]*size
        # self.map = [LinkedList()]*size
        # self.map = [[]]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key: #get sum for asccii codes
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*193
        indx = temp%self.size
        return indx

    def set(self, key):
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
        array=string.split()
        for i in array:
           self.set(i)


    def Repeated_Word(self,string):
        x=string.split()
        for i in x:
            hashed_key = self.custom_hash(i)
            
            if self.map[hashed_key] and isinstance(self.map[hashed_key], LinkedList) :
                # print(i,hashed_key,self.map[hashed_key].duplicate_node(i))
                if self.map[hashed_key].duplicate_node(i):
                    # print(i)
                    return i
        # print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        return "No Repetition"




if __name__ == "__main__":
    hashtabel1 = HashTabel()
    st="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    hashtabel1.create_hashTable_from_string(st)
    # print(array)
    # for i in array:
    #     hashtabel1.set(i)

    # hashtabel1.set("C",10)
    print("print the hashtable ")
    print(hashtabel1.map[0])
    print(hashtabel1.map[1])
    print(hashtabel1.map[2])
    print(hashtabel1.map[3])
    print(hashtabel1.map[4])
    print("*********************************************************")
    print("Repeated Word:  " ,hashtabel1.Repeated_Word(st))

    
