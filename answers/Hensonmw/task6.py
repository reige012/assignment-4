#!/usr/bin/env python
# encoding: utf-8

"""
    My six program for Assignment 4
    
    Created by Michael Henson on 27 Jan 2016.
    Copyright 2016 Michael W Henson. All rights reserved.
    
"""


from numpy import array

from Bio.Seq import Seq


#Now lets try and make two functions and then have type() tell us what it they are.
##btw don't name your function the same as something you are importing
###because then you get stupid errors that you spends lot of time on that were easy to fix

def testing():
    Bulldogsucks = array([2, 10, 10, 12])
    print(Bulldogsucks)
    print(type(Bulldogsucks))

#make a sequence and then have type() say what it is


def bacteria():
    dna_seq = Seq("AGTACACTGGT")
    print(dna_seq)
    print(type(dna_seq))

#lets run them both

def main():
    testing()
    bacteria()


if __name__ == '__main__':
    main()

