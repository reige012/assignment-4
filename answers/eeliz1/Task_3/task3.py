#!/usr/bin/env python
# encoding: utf-8

#Lists every 5th number from 50 to 0#

list1=list(range(0,51,5))
def reverse(list1):
    output = []
    for i in range (len(list1) -1, -1, -1):
        output.append(list1[i])
    return output
print(reverse(list1))
