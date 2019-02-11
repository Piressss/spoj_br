#!/usr/bin/env python

import sys

v=1
b50=0
b10=0
b5=0
b1=0
tmp=0
j=0
tmp_res=[]
result=0

v=int(raw_input())

while v != 0:
    tmp_res.insert(0,v / 50)
    tmp = v % 50
    tmp_res.insert(1,tmp / 10)
    tmp = tmp % 10
    tmp_res.insert(2,tmp / 5)
    tmp = tmp % 5
    tmp_res.insert(3,tmp / 1)
    v=int(raw_input())
    if v != 0:
        j=j+1


    if v == 0:
       tmp_res.reverse()
       print '\n'
       for i in range(j+1):
          print 'Teste', i+1
          result = tmp_res[i*4:4+4*i]
	  print result[3], result[2], result[1], result[0], '\n' 
