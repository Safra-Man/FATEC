#-*- coding:utf-8 -*-

print('****N é Triangular?****\n')

n=int(input('Digite N: '))
a=1
b=2
c=3

prod=0

while prod<n:
	prod=a*b*c
	if prod>n:
		print('\nN não é Triangular!')
	elif prod==n:
		prod=n
		print('\nN é Triangular!')
	else:
		a=a+1
		b=b+1
		c=c+1

input()

