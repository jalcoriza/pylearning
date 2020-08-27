#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
i=2
nprimes=1
primes=[2]
print(nprimes,i, 'prime')
while nprimes<100:
    prime=True
    for j in primes:
        k=i%j
        if k==0:
            prime=False
            break
    if prime:
        primes.append(i)
        nprimes+=1
        print(nprimes,i, 'prime')
    i+=1