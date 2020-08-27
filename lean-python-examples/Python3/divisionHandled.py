#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
print('Input two numbers. The first will be divided by the second')

afirst = input('first number:')
asecond = input('second number:')

try:
    first=float(afirst)
    second = float(asecond)
    quotient = first / second
    print('Quotient first/second = ',quotient)
except Exception as diag:
    print(diag.__class__.__name__,':',diag)
    
