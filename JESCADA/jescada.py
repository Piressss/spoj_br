#!/usr/bin/env python

import sys

tt=0

# numero de pessoas na escada
num=int(raw_input())

for i in range(num):
    ti=int(raw_input()) # tempo que a pessoa passa pelo sensor
    if i==0:
        tf0=ti
    else:
        tf0=tf
    tf=ti+10
    if (tf-tf0) > 10:
        tt=tt+10
    else:
        tt=tt+tf-tf0
    #print "HERE", "ti=", ti, "tf=", tf, "tt=", tt

print tt
