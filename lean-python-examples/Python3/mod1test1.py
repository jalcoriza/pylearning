#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
import mod1 as m1

m1.hello()
print('written by', m1.writtenby)

greet = m1.greeting()
greet.morning()
greet.evening()