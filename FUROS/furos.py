#!/usr/bin/env python

import sys
import math
import timeit

#Funcao para calcular o diametro
def diametro(centro=[],furo=[]):
    #calcula a distancia em X e Y
    x=furo[0]-centro[0]
    y=furo[1]-centro[1]
    #normalizo pois os valores nao podem ser negativos
    if x < 0:
        x=x*(-1)
    if y < 0:
        y=y*(-1)
    #somo o diametro do furo
    if x != 0:
        x=(x+2)
    if y != 0:
        y=(y+2)
    #calculo a distancia pela formula da hipotenusa
    if x != 0 and y != 0:
        x=(x**2)
        y=(y**2)
        result=(math.sqrt(x+y))*2
    else:
        result=(x*2)+(y*2)
    result=math.ceil(result)
    return result

#Funcao de leitura para inteiro
def readint():
    result=int(str.split(raw_input())[0])
    return result

def read2int():
    del result[:]
    tmp=raw_input()
    tmp=tmp.split(" ")
    for i in range(2):
        result.append(int(tmp[i]))
    return result

#os dados dos furos serao armazenados em uma funcao tri-dimensional
read=[0,0]
furos=[]
furos_3d=[]
result=[]
tresult=[]
calc=[]
tmp=0
z=0

while 1:

    #Entrada de dados
    nteste=readint()
    #Verifico se zero
    if nteste == 0:
        break;
    #Pego as informacoes para os calculos
    for i in range(nteste):
        furos = furos[:]+read2int()
    #Preciso refazer a lista para ter uma lista 3-dimensional
    for i in range(0,nteste*2,2):
        furos_3d.append(furos[i:i+2])
    #Executo os calculos colocando como centro cada um dos furos
    for i in range(nteste):
        calc.append(0)
        for j in range(1,nteste):
            tmp=(diametro(furos_3d[0],furos_3d[j]))
            if tmp > calc[i]:
                calc[i] = tmp
        furos_3d=furos_3d[len(furos_3d)-1::]+furos_3d[:len(furos_3d)-1:]
    # Com os maiores valores para as distancias encontradas com cada possivel centro,
    # agora achamos o menor entre eles
    #Finalizado para o primeiro teste, repetimos o laco ate o ultimo teste
    tresult.append(int(min(calc)))
    del furos[:]
    del furos_3d[:]
    del calc[:]
    z=z+1

#Mostramos o resultado
print("")
for i in range(z):
    print("Teste %i" %(i+1))
    print("%i\n" %tresult[i])
