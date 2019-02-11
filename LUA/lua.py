#!/usr/bin/env python

import sys

y=[] # medidas de entrada
m=[] # medias
m_max=[]
m_min=[]
media=0
x = str.split(raw_input())  # numero de medidas e o intervalo para media

while int(x[0]) != 0:
    # vamos receber as medidas e calcular as medias
    for i in range(int(x[0])):
        y.append(raw_input())
    for i in range(int(x[0]) - int(x[1]) + 1):
        for j in range(i,i+int(x[1])):
            media=int(y[j])+media
        media=media/int(x[1])
        if media < 0:
            #media=-1*(-1*media/int(x[1]))
            #media=-1*media
            media=media+1
        #elif media >= 0:
            #media=media/int(x[1])
        m.append(media)
        media=0
        
    m_max.append(max(m))
    m_min.append(min(m))
    for i in range(len(y)):
        y.pop()
    for i in range(len(m)):
        m.pop()
    media=0
    x = str.split(raw_input())
    
for i in range(len(m_max)):
    print "Teste ", i+1, '\n', int(m_min[i]), int(m_max[i]), '\n'
