#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
import requests
import re         # The RegEx library
#
#   this code opens a connection to the leanpy.com website
#
response = requests.get('http://leanpy.com')
data1 = str(response.content)           # put response text in data
#
#   our regular expression (to find links)
#
regex = '<a\s[^>]*href\s*=\s*\"([^\"]*)\"[^>]*>(.*?)</a>'
#
#   compile the regex and perform the match (find all)
#
pm = re.compile(regex)
matches = pm.findall(data1)
#
#   matches is a list
#   m[0] - the url of the link
#   m[1] - text associated with the link
#
for m in matches:
    ms=''.join(('Link: "',m[0],'" Text: "',m[1],'"'))
    print(ms)
