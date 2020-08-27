#!/usr/bin/env python3
#
#  Copyright (c) 2015 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
import requests
from urllib.parse import urlparse

path=''
url=input('Web url to fetch:')
urlparts=urlparse(url)
if urlparts[0]=='':
    url=''.join(('http://',url))
print(str(urlparts))

qstring=input('Enter query string:')

save=input('Save downloaded page to disk [y/n]?')
if len(qstring)>0:
    url='?'.join((url,qstring))
    
print('Requesting',url)

try:
    response = requests.get(url)
    if save.lower()=='y':
        geturl=response.url
        urlparts=urlparse(geturl)
        print('URL:',urlparts)

        if urlparts.path == '/':
            fname='save.html'
        else:
            fname='_'.join(path.split('/'))
            fname='_'.join(path.split('\\'))
            fname='.'.join((fname,'html'))
        print('saving to',fname,'...')
        fp=open(fname,'w')
        fp.write(response.content.decode(encoding='UTF-8'))
        fp.close()
    else:
        print(response.content)
except Exception as e:
    print(e.__class__.__name__,',',e)


