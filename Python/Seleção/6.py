#-*- coding:utf-8 -*-

print('****Fórmula de Bhaskara****')

a=float(input('Digite A: '))
b=float(input('Digite B: '))
c=float(input('Digite C: '))

delta=(b**2)-(4*a*c)

print('Delta: ',delta)

if delta<0:
    print('Não existem Raízes Reais')
    input()
else:
    b=-b
    delta=delta**0.5
    x1=(b+delta)/(2*a)
    x2=(b-delta)/(2*a)

    print('Raiz x1: ',x1)
    print('Raiz x2: ',x2)
    input()







