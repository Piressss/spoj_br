#!/usr/bin/env python

import sys
import math
import timeit

def value(p1=[],p0=[]):
    res=math.hypot(int(p1[0])-int(p0[0]),int(p1[1])-int(p0[0]))
    return res

# x=[]
# y=[]
tmp=[]
min_v=2000000

num=int(str.split(raw_input())[0])
for i in range(num):
    tmp.append(str.split(raw_input()))
    # x.append(tmp[0])
    # y.append(tmp[1])
    
for j in range(num):
    for z in range(j+1,num):
        # r1=int(x[z])-int(x[j])
        # r2=int(y[z])-int(y[j])
        # r0=math.sqrt((r1**2)+(r2**2))
        # r0=math.sqrt(((int(x[z])-int(x[j]))**2)+((int(y[z])-int(y[j]))**2))
        # r0=math.hypot(int(x[z])-int(x[j]),int(y[z])-int(y[j]))
        # if abs(math.hypot(int(tmp[z][0])-int(tmp[j][0]),int(tmp[z][1])-int(tmp[j][1]))) < min_v:
        if abs(value(tmp[z],tmp[j])) < min_v:
        # if abs(r0) < min_v:
            min_v=math.hypot(int(tmp[z][0])-int(tmp[j][0]),int(tmp[z][1])-int(tmp[j][1]))
            
print ("\n%.3f" %min_v)