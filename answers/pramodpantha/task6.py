#!/usr/bin/env python
# utf-8

"""
 program with a main function that calls two separate functions to show the
 type of numpy array and sequence object (from biopython).
Created by Pramod Pantha on 28 Jan, 2016.
Copyright 2016 Pramod Pantha. All right reserved.

"""


def type_numpy():
    import numpy as np
    A = np.array([0, 10, 20, 30])
    print(A)
    print(type(A))


def type_seq():
    from Bio.Seq import Seq
    seq = Seq("ATGCCGTAATGC")
    print(seq)
    print(type(seq))


def main():
    type_numpy()
    type_seq()


if __name__ == '__main__':
    main()
