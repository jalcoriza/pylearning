#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
def analyse(numlist):

    nmin = nmax = None
    navg = nsum = 0.0
    if len(numlist) > 0:
        for n in numlist:
            nsum += n
            if nmin is None or n < nmin:
                nmin = n
            if nmax is None or n > nmax:
                nmax = n
        navg = nsum / len(numlist)
    
    return nmin, nmax, navg, nsum
#
#   to create automated unit tests, it's easier to have a 
#   test driver that returns a single variable, so 
#   this function packages the four return values into a
#   tuple for comparison
#    
def testAnalyse(numlist):
    nmin, nmax, navg, nsum = analyse(numlist)
    #
    #   return four values as a tuple
    #
    return (nmin, nmax, navg, nsum)
    
        
