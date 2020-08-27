#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
print('Input two numbers. the first will be divided by the second')

afirst = input('first number:')
first=float(afirst)
asecond = input('second number:')
second = float(asecond)

quotient = first / second
print('Quotient first/second = ',quotient)
