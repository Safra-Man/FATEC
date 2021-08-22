#-*- coding:utf-8 -*-

print('****Acha o M.D.C pelo Algoritmo de Euclides****\n')

n1=int(input('Digite o 1º Valor: '))
n2=int(input('Digite o 2º Valor: '))

if n2>n1:
	r=n1
	n1=n2
	n1=r
else:
	r=n1


while r!=0:
	r=n1%n2
	if r==0:
		break
	n1=n2
	n2=r

	
	

print('O M.D.C é: %i'%n2)


	















	
		
input()

