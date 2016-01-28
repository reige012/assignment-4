#!/usr/bin/env python
# encoding: utf-8
"""
First script for a program.
This is one step close to my this year's resolution.

Created by Mukesh Maharjan on 26 Jan 2016.
Copyright 2016 Mukesh Maharjan. All rights reserved.

"""
import numpy
import Bio
from Bio.Seq import Seq


my_seq = Seq('AGTACACTGGT')
ans = numpy.arange(10)


def seq():
    print(type(my_seq))

def numpy():
        print(type(ans))


def main():
    seq()
    numpy()

main()
