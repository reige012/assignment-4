#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 4, Task 6
Austen T. Webber
2016_01_27
"""

# Import required packages
import numpy
from Bio.Seq import Seq

# vols_5() prints type of numpy array
def vols_5():
    boom = array([0, 2, 4, 6, 8, 10])
    print(boom)
    print(type(boom))

# vols_6() prints type of sequence from BIOPYTHON
def vols_6():
    test = Seq("ATGCGACGCAGCGACGCAGCGACGCGACGCAGCAGCGACGCAGCGCGACGACGACGACGCTCATCATCTACTCAGCAGCATCAGCATCAGACT")
    print(test)
    print(type(test))

# The main function calls vols_5() and vols_6()
def main():
    vols_5()
    vols_6()

if __name__ == '__main__':
     main()
