# !/usr/bin/env python
# encoding: utf-8

"""
My fantastic stringy program

Created by Andre Moncrieff on 27 Jan 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

"""

def favWordAdder(a, b, c, d, e):
    fav_words = [a, b, c, d, e]
    return '\n'.join(fav_words)
    
    
def main():
    answer = favWordAdder(a = "putative",b = "scrumptious", c = "juicy", d = "sweet", e = "however")
    print(answer)

if __name__ ==  '__main__':
    main()