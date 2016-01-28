#!/usr/bin/env python
# utf-8

"""
Task 6 Program
Jessie Salter
26 January 2016
"""

# First, I will import the modules I need for this program

from numpy import array

from Bio.Seq import Seq


# jsalt5() defines an array and prints the array and its type.


def jsalt5():
    x = array([0, 5, 10, 15])
    print(x)
    print(type(x))


# jsalt6() defines a sequence object and prints the sequence and its type.


def jsalt6():
    my_seq = Seq("AGTACACTGGT")
    print(my_seq)
    print(type(my_seq))


# The main function calls jsalt5() and jsalt6()


def main():
    jsalt5()
    jsalt6()


if __name__ == '__main__':
    main()
