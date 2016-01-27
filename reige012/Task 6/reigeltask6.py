#!/usr/bin/env python
# #encoding: utf-8

"""
This program is used to find the types for two functions: one from numpy
and one from biopython's Seq program.

Created by Alicia Reigel. 26 January 2016.
No copyright...anyone can use this.

"""
def anump():
    import numpy
    alicianumpy=numpy.arange(0, 10, 1)
    print (alicianumpy)
    print (type(alicianumpy))

def reigbio():
    from Bio.Seq import Seq
    alicia_seq=Seq("ACCTGAAACGCGTGCAATTC")
    print(alicia_seq)
    print (type(alicia_seq))

def main():
    anump()
    reigbio()

if __name__ == '__main__':
    main()
