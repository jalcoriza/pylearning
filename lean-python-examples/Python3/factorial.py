#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
fac = 1
fp = open('factorials.txt','w')
for i in range(1,101):
    fac *= i
    text = ' '.join((str(i),'Factorial is',str(fac),'\n'))
    fp.write(text)
fp.close()
