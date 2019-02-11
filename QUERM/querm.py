#!/usr/bin/env python

import sys

x=1 # numeros de participantes
y=[]   # array para as entradas dos participantes
j=0 
result=[] # variavel para armazenar o resultado

x=int(raw_input())

while x != 0:
    y=raw_input()
    y=str.split(y)
    for i in range(x):
	if int(y[i]) == (i+1):      
            result.append(i+1)
    x=int(raw_input())
    if x != 0:
        j=j+1

print '\n'
for i in range(j+1):
    print 'Teste', i+1
    print result[i], '\n'

