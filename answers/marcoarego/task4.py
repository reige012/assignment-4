# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:58:33 2016

@author: Marco
"""

"""
Task 4

String operations are great and lots of fun. You'll be dealing with strings a 
lot (more fun awaits when we specifically talk about strings). Write a program 
with a main function that calls a separate function (name of your choice) to 
print your 5 favorite words, separated by newlines.
"""

def main():
    # I nested one function inside the other
    def words():
        # In this function I used the \n to define new Lines. It worked on Spyder
        print ("jaguara\nroça\nmaloca\npaçoca\nglau")
    return words()
    
if __name__=='__main__':
    main()