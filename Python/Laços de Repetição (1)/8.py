#-*- coding:utf-8 -*-

print('****Soma n Números despois de n****')

n=int(input('N: '))
s=0
n1=n

while n1<(2*n):
	n1=n1+1
	s=s+n1
	print(n1)
print('Temos %i como soma de Todos N exibidos'%s)
