#!/usr/bin/env python

import sys 
import re

def mysplit(mystr):
    return re.split("([+-])", mystr.replace(" ", ""))

m = 1 # Inicializacao da variavel
j = 0
x=[]
r=[]

m=int(raw_input())

while m != 0:   
    x=raw_input()
    l=mysplit(x)
    
    for i in range(0,len(l),2):
        if i == 0:
            r.append(l[i])
        else:
            if l[i-1] == '+':
                r[j]=int(r[j])+int(l[i])
	    elif l[i-1] == '-':
		r[j]=int(r[j])-int(l[i])
    
    j=j+1
    m=int(raw_input())

for i in range(j):
    print 'Teste', i+1
    print r[i], '\n'
    
    
