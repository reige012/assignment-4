#!/usr/bin/env python
# encoding: utf-8

"""
Created by Yuankai Dong on 1/27/2016
Copyright 2016 Yuankai Dong. All rights reserved.

"""

def my_first_function():
    import numpy as np
    a=np.array([1, 2, 3])
    type(a)
def my_second_function():
    from BioPython import Seq
    from Bio.Alphabet import IUPAC
    my_seq = Seq("TTCACACTCAT", IUPAC.unambiguous_dna)
    type(my_seq)

def main():
    my_first_function()
    my_second_function()

if __name__ == '__main__':
        main()
