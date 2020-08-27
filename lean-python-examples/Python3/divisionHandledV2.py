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
try:
  first=float(afirst)
  asecond = input('second number:')
  try:
    second = float(asecond)
    try:
      quotient = first / second
      print('Quotient first/second = ',quotient)
    except ZeroDivisionError as diag:
      print(diag,': Second number must be non-zero')
  except ValueError as diag:
    print(diag,'Second number')
except ValueError as diag:
    print(diag,'First number')