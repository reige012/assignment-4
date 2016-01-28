#!/usr/bin/env python
# encoding: utf-8

"""
My third program for Assignment 4

Created by Michael Henson on 27 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
#Now lets reverse them using reversed...there is also a way with negative numbers but couldn't figure it out.

def legitreversed_code():
	X = range(0,51,5)
	print(list(reversed(X)))

def main():
    legitreversed_code()
    
if __name__ == '__main__':
    main()