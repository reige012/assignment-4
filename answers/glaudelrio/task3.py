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
Task 3

Modify the program you created in Task 2 to print the numbers out in reverse
order (highest to lowest).

"""

def print_50_to_0_by_5():
    zero_to_50 = list(range(0,51,5))
    #reversing the order of the numbers in the range: 
    print(list(reversed(zero_to_50)))


def main():
    return print_50_to_0_by_5()


if __name__ == '__main__':
    main()
