# !/usr/bin/env python
# encoding: utf-8

"""
My type-showing program

Created by Andre Moncrieff on 27 Jan 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

"""

import numpy
from Bio.Seq import Seq
            

def getArrayType():
    list_1 = [11,12,13,14]
    array_1 = numpy.array(list_1)    
    return type(array_1)

def getSeqObjType():
    made_up_sequence = Seq("AGTCCCCATATGCGA")
    return type(made_up_sequence)
    
def main():
    print("Type of numpy array is: ")
    print(getArrayType())
    print("Type of a sequence object is: ")
    print(getSeqObjType())
    

if __name__ ==  '__main__':
    main()
    
 
    
    
