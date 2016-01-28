# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:41:32 2016

@author: Marco
"""

"""
Task 2

Based on what you wrote, above, create another program with a main function
that calls a separate function (name of your choice) to print out the same 
information requested in Task 1.
"""


def main():
    # I nested one function inside the other
    def get_numbers():
        # creating a list with the numbers in the desired range
        print([elem for elem in range(0,51,5)])
    return get_numbers()

if __name__=='__main__':
    main()