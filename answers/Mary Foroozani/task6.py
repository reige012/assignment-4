#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2
"""


def type_numpy():
    import numpy as np
    a = np.array([1, 2, 3])
    print(type(a))


def type_seq():
    from Bio.Seq import Seq
    my_ChIP_seq = Seq("AGTACACTGGT")
    print(type(my_ChIP_seq))


def main():
    type_numpy()
    type_seq()


if __name__ == '__main__':
    main()
