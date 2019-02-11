#!/usr/bin/env python

import sys
import math
import timeit

def dobra(ndobra):
    if ndobra == 0:
        result = 4
    else:
        result = (4**ndobra)+(2**(ndobra+1))+1
    return result

result=[]
i = 0

while 1:

    ndobra = int(str.split(raw_input())[0])
    if ndobra == -1:
        break;
    result.append(dobra(ndobra))
    i=i+1

print("\n")

for j in range(i):
    print("Teste %i" %(j+1))
    print(result[j])
    print("\n")

