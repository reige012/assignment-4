# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:21:39 2016

@author: Glaucia
"""
"""
Task 5

In Task 4, you basically concatenated strings. 
There are several ways to do this. Alter the program that you wrote above to
print your 5 favorite words, separated by newlines, but do this in a different 
way from how you did it in Task 4.

"""
def print_my_favorite_words2():
   #printing my favorite words one at a time:
    print("Ei")
    print("mucurinha")
    print("bora")
    print("Amazônia")
    print("Tumbira")

#calling the previous function in the main function:
def main():
    #returning the results of print_my_favorite_words function
    return print_my_favorite_words2()

    
if __name__ == '__main__':
    main()
