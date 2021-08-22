#-*- coding:utf-8 -*-

print('****Possui ou Não Possui Algarismos Pares ou Ímpares Adjacentes****\n')

n=int(input('Digite o Valor de N>10: '))
a=n
i=int(0)

while a!=0:
	a=a//10  # Acha a qtd de caracteres i
	i=i+1
	

first=n//(10**(i-1))  # Isola o primeiro membro

last=n%10

if (first%2==0 and last%2==0) or (first%2!=0 and last%2!=0):
	print('\nNão Possui')
else:
	print('\nPossui')

input()

