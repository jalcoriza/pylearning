#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
from mod1 import greeting,hello,writtenby

hello()
hello.writtenby='xxx'
print('written by', hello.writtenby)
print(writtenby)

greet = greeting()
greet.morning()
greet.evening()