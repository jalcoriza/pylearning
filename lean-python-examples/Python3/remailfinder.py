#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
import re         # The RegEx library
#
#	the emails.txt file contains some junk messages.
#   the text contains emails of the form <x@y.z>
#   so we add <> to the leading and trailing 
#   character matches. These are not stripped off 
#   by strip(). Perhaps you could enhance the code
#   to do this?
#
#   Our regular expression (to find emails)
regex = '[\s<>][A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s<>]'

fp = open('emails.txt','r')
text=fp.read()
fp.close()

# print('** Search text ***\n'+text)
print('** Regex ***\n'+regex+'\n***')
#
#   uppercase our text
utext=text.upper()
#
#   perform a search
s = re.search(regex,utext)
if s:
    print('Search found: '+s.group())
#
#   find all matches
m = re.findall(regex,utext)
if m:
    for match in m:
        print('Match found',match.lower().strip())
