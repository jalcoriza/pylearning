#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
from __future__ import print_function
import re         # The RegEx library
#
# our regular expression (to find emails)
# and text to search
#
regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]'
text="""This is some text with x@y.z embedded emails
that we'll use as@example.com
some lines have no email @ddresses
others@have.two valid email@addresses.com
The re module is awonderful@thing."""
print('** Search text ***\n'+text)
print('** Regex ***\n'+regex+'\n***')
#
#   uppercase our text
utext=text.upper()
#
#   perform a search (any emails found?)
s = re.search(regex,utext)
if s:
    print('*** At least one email found "'+s.group()+'"')
#
#   now, find all matches
#
m = re.findall(regex,utext)
if m:
	for match in m:
		print('Match found',match.strip())
