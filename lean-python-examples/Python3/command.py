#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
from __future__ import print_function
import sys

nargs=len(sys.argv)
print('%d argument(s)' % (nargs))
n=0
for a in sys.argv:
    print('  arg %d is %s' % (n,a))
    n+=1
