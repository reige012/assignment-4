#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 4 Task 6

Amie Settlecowski
28 Jan. 2016

"""


import numpy as np
import Bio.Seq
import Bio.Alphabet


def type_nparray(o):
    typ = o.dtype
    print(typ)


def type_bioseq(o):
    typ = type(o)
    print(typ)


def main():

    a = np.array([(1, 2, 3), (4, 5, 6)])
    type_nparray(a)

    s = Bio.Seq.Seq('ATCGATCNATCG', Bio.Alphabet.IUPAC.ambiguous_dna)
    type_bioseq(s)

if __name__ == '__main__':
    main()
