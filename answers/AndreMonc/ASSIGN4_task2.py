# !/usr/bin/env python
# encoding: utf-8

"""
My calling program

Created by Andre Moncrieff on 27 Jan 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

"""

def seriesmaker(x, y, z):
    example = (list(range(x,y,z)))
    excise = (str(example).strip('[]'))
    return excise
    
def main():
    answer = seriesmaker(0, 51, 5)
    print(answer)

if __name__ ==  '__main__':
    main()