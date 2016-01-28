# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:08:22 2016

@author: Marco
"""

"""
Task 6
We talked a little bit about types. Write a program with a main function that 
calls two separate functions to show the type of (1) a numpy array, and (2) a 
sequence object (from biopython).
"""

# Importing modules
import numpy
from Bio.Seq import Seq

# Function to get numpy array type
def numpy_type():
    number_list = numpy.array([1,2,3])
    print(type(number_list))
# Function to get Bio Sequence Type
def bio_seq_type():
    word = Seq("banana")
    print(type(word))
# Main Function that runs the previous functions
def main():
    print ("Biopython Sequence Type")
    bio_seq_type()
    print ("Numpy Array Type")
    numpy_type()
# Magic piece of code
if __name__ == '__main__':
    main()
