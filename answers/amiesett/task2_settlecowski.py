#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 4 Task 2

Amie Settlecowski
28 Jan. 2016

"""


def print_range(start, stop, step):
    return_list = [str(n) for n in range(start, stop, step)]
    print(','.join(return_list))


def main():

    print_range(0,51,5)

if __name__ == '__main__':
    main()
