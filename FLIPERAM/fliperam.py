#!/usr/bin/env python

import sys
import re

pts=[]

num_in=raw_input()

num_in=str.split(num_in)

for i in range(int(num_in[0])):
    pts.append(int(raw_input()))

pts.sort(reverse=True)
#print pts

print "\n"
for i in range(int(num_in[1])):
    print pts[i] 
