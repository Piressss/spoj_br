#!/usr/bin/env python

# Algoritmo de Miller-Rabin

import sys

from random import *

i=1
x=0
a=0
k=0
q=0
n=int(raw_input()) #Entrada do numero para teste de primalidade

# No caso da entrada ser igual a 1, 2 ou 3 ja jogamos que eh primo diretamente
if (n <= 3):
    print "sim"
    exit(0)

x=(n-1)
x=x/2

# vamos fatorar a metade de X para achar o valor de q e k
while((x % 2) == 0):
    x=x/2
    i=i+1
    
q=x
k=i

# seleciono um numero aleatorio 'a' inteiro e testo para satisfazer as seguintes propriedades
a=randint(2,n-1)

# verifico se eh inconclusivo o resultado
if ((a**q) % n) == 1 :
    print "sim"
    exit(0)
    
for i in range(k-1):
    if ((a**((2**i)*q)) % n) == (n-1):
        print "sim"
        exit(0)

print "nao"
