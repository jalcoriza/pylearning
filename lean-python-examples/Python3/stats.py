#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
from analyse import analyse

numlist = []

while True:
    nextnum = input('Enter a number or blank line:')
    if len(nextnum) == 0:
        break
#
#   try and obtain a floating point number from the input
#
    try:
        num = float(nextnum)
        numlist.append(num)
    except:
        print(nextnum, 'is not numeric')

nmin, nmax, navg, nsum = analyse(numlist)

print(nmin, nmax, navg, nsum)


