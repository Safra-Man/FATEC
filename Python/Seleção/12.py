#-*- coding:utf-8 -*-

print('****O Quadrado se Esconde no Círculo?****')

#Area do Circulo = Pi*Raio**2 
#Diametro do Circulo = 2*Raio
#Area do Quadrado = l**2
#Diametro do Quadrado = l*(2**0.5) 
#Pi=3,1415926535

ac=float(input('Área do Círculo: '))
aq=float(input('Área do Quadrado: '))

pi=3.1415926535

dc=2*((ac/pi)**0.5)
dq=(aq**0.5)*(2**0.5)

if dq<=dc:
    print('O Quadrado se esconde sob o Círculo!')
else:
    print('O Quadrado NÃO se esconde sob o Círculo!')

input()