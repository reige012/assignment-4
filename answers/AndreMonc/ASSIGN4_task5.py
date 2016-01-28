# !/usr/bin/env python
# encoding: utf-8

"""
My second fantastic stringy program

Created by Andre Moncrieff on 27 Jan 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

"""

def favWordAdder(a, b, c, d, e):
    fav_words = [a, b, c, d, e]
    for num in range(5):
        word = fav_words[num]
        print(word)
            
def main():
    favWordAdder(a = "putative",b = "scrumptious", c = "juicy", d = "sweet", e = "however")

if __name__ ==  '__main__':
    main()