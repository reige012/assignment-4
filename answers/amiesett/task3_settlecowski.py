#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 4 Task 3

Amie Settlecowski
28 Jan. 2016

"""


def print_reverse(start, stop, step):
    return_list = [str(n) for n in reversed(range(start, stop, step))]
    print(','.join(return_list))


def main():
    print_reverse(0, 51, 5)

if __name__ == '__main__':
    main()
