# Write your test here
import pytest 
from linked_list import LinkedList,Node
from challenge02 import HashTabel,Repeated_Word

# test if the linked list empty

# test if the number of node inside linked list is even



def test_one():   
    hashtabel1 = HashTabel()
    st="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    assert Repeated_Word(st,hashtabel1)=="ASAC"


def test_two():   
    hashtabel1 = HashTabel()
    st=""
    assert Repeated_Word(st,hashtabel1)=="No Repetition"


def test_three():   
    hashtabel1 = HashTabel()
    st="I am learning programming at ASAC"
    assert Repeated_Word(st,hashtabel1)=="No Repetition"


def test_HashTabel_str():
    hashtabel1 = HashTabel()
    st="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    hashtabel1.create_hashTable_from_string(st)

    assert hashtabel1.__str__()=="0 :[['ASAC'], ['is'], ['ASAC'], ['in']] \n1 :[['a'], ['programming']] \n2 :None \n3 :['department'] \n4 :[['at'], ['LTUC.'], ['teaches'], ['LTUC.']] \n"
    
   