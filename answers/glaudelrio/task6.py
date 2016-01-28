# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:27:20 2016

@author: Glaucia
"""
"""
Task 6

We talked a little bit about types. Write a program with a main function that 
calls two separate functions to show the type of (1) a numpy array, and (2) a 
sequence object (from biopython).
"""
#importing numpy and Bio.Seq
import numpy
import Bio.Seq

def array_BioSeqSeq():
    #using the type function to get the type of the numpy array   
    print(type(numpy.array([0,5,10,15,20])))
    #using the type function to get the type of the sequence object (Bio.Seq.Seq)  
    print(type(Bio.Seq.Seq("ATATATAAT")))
    
#calling the previous function in the main function:
def main():
    #returning the results of array_BioSeqSeq function
    return array_BioSeqSeq()

    
if __name__ == '__main__':
    main()
