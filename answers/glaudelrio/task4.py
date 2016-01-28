# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:57:57 2016

@author: Glaucia
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:06 2016

@author: Glaucia
"""
"""
Task 4

String operations are great and lots of fun. 
You'll be dealing with strings a lot (more fun awaits when we specifically 
talk about strings). Write a program with a main function that calls a separate
function (name of your choice) to print your 5 favorite words, 
separated by newlines.

"""

def print_my_favorite_words():
    #creating a list with my five favorite words and assigning it to the variable "words"
    words = ["ei","mucurinha","bora","Amazônia","Tumbira"]
    #for loop to get each of my words (strings) in the list "words"
    for word in words:
        #print each of my words in a new line
        print(word)

#calling the previous function in the main function:
def main():
    #returning the results of print_my_favorite_words function
    return print_my_favorite_words()

    
if __name__ == '__main__':
    main()


