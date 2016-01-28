#! /usr/bin/env python
# encoding: utf-8


'''
Printing Backwards is Fun by Grace Cagle

Printing numbers 50 -> 0 by 5

Function name is back50

'''


def back50():
    a = list(range(0, 55, 5))
    for i in reversed(a):
        print(i)

if __name__ == '__main__':
    back50()
