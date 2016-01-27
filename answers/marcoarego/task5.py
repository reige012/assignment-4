# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:05:09 2016

@author: Marco
"""

"""
Task 5

In Task 4, you basically concatenated strings. There are several ways to do 
this. Alter the program that you wrote above to print your 5 favorite words, 
separated by newlines, but do this in a different way from how you did it in 
Task 4.
"""


def main():
    # I nested one function inside the other
    def words():
        # I will loop over strings in a list to print each value on a different line
        for word in ["jaguara","roça","maloca","paçoca","glau"]:
            print (word)
    return words()
    
if __name__=='__main__':
    main()