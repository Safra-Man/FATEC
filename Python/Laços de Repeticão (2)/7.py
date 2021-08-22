#-*- coding:utf-8 -*-

print('****É Primo ou Não?****\n')

n=int(input('Digite o Valor para Verificar: '))

i=1
a=n

while a!=1:
	a=n//i
	i=i+1
	if n//i==1:
		print('É Primo')
		break
	elif n%i==0:
		print('Não é Primo')
		break
	
input()

