#-*- coding:utf-8 -*-

print('****Inverte Algarismos****\n')

n=int(input('Digite o Valor para Inverter: '))
a=n
i=int(0)

while a!=0:
	a=a//10  # Acha a qtd de caracteres i
	i=i+1

n1=0

while i!=0:
	n1=n%10
	n=(n-n1)//10
	print(n1,end="")
	i=i-1

input()

