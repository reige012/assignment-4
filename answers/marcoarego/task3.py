# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:41:32 2016

@author: Marco
"""

"""
Task 3
Modify the program you created in Task 2 to print the numbers out in reverse 
order (highest to lowest)
"""


def main():
    # I nested one function inside the other
    def get_rev_numbers():
        # I used the reversed function to reverse the list
        print([elem for elem in reversed(range(0,51,5))])
    return get_rev_numbers()
    
if __name__=='__main__':
    main()