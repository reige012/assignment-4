#!/usr/bin/env python
# utf-8

"""
Task 3 Program
Jessie Salter
26 January 2016
"""

# jsalt2() will print the numbers 0 to 50 by 5 in reverse order


def jsalt2():
    print(list(reversed(range(0, 55, 5))))


# The main function calls the jsalt(2) function


def main():
    jsalt2()


if __name__ == '__main__':
    main()
