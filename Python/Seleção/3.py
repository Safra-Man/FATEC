#-*- coding:utf-8 -*-

a=int(input('A: '))
b=0
c=int(input('B: '))

n=int(input('n: '))


if c<a:
    b=a
    a=c
else:
    b=c


if a<n<b:
    print('No intervalo')
else:
    print('Fora do intervalo')





