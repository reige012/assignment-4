#!/usr/bin/env python
# encoding: utf-8

"""
My six program for Assignment 4

Created by Michael Henson on 27 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
#Now lets try and make two functions and then have type() tell us what it they are.

import numpy import array
from Bio.Seq import Seq

def data_array():
	Bulldogssuck= array([2,2,2,6,6,6])
	print(Bulldogssuck)
	print(type(Bulldogssuck)

def data_seq():
	bacteria = Seq("AGTGGGCGACGAGTGGCGAACGGCTG")
	print(bacteria)
	print(type(bacteria))


def main():
	data_array()
    data_seq()

if __name__ == '__main__':
    main()