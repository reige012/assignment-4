# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:06 2016

@author: Glaucia
"""
"""
Task 2

Based on what you wrote, above, create another program with a main function
that calls a separate function (name of your choice) to print out the same
information requested in Task 1.

"""
#separate function that is printing the expected range such as in task 1:
def print_0_to_50_by_5():
    print(list(range(0,51,5)))

#defining the main function that calls the separate function above:
def main():
    return print_0_to_50_by_5()

#executing the function every time the task2 is run:
if __name__ == '__main__':
    main()
