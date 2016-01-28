#!/usr/bin/env python
# encoding: utf-8

"""
program task 6. Assignment 4

Jon Nations. 27 January 2016

"""
def numpy():
   import numpy
   a=numpy.array([1,2,3])
   print (type(a))

def bioseq():
    import Bio
    from Bio.Seq import Seq
    my_seq = Seq('CATA')
    print (type(my_seq))


def main():
   numpy()
   bioseq()

if __name__ == '__main__':
       main()
