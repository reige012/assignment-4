#! /usr/bin/env python
# encoding: utf-8
'''
Type of a numpy array and sequence object from biopython

'''

import numpy as np
from Bio import Seq
my_seq = Seq("AGTACACTGGT")
# this is my numpy array
np_array = np.array([1, 2, 3])
# this is my sequence object


def type(thing):
    print(type(thing))

if __name__ == '__main__':
    type(np_array)
    type(my_seq)
