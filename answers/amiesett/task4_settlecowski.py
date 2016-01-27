#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 4 Task 4

Amie Settlecowski
28 Jan. 2016

"""


def word_print(w_list):
    return_list = w_list
    for w in return_list:
        print(w)


def main():

    word_list = ["y'all","boil","supper","pecan","crayfish"]
    word_print(word_list)

if __name__ == '__main__':
    main()
