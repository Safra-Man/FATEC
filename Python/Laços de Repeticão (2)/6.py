#-*- coding:utf-8 -*-

print('****Mostra se Números estão em Ordem Crescente****\n')

n=int(input('Digite o Valor para Verificar: '))

a=n
i=0

while a!=0:
	a=a//10  # Acha a qtd de caracteres i
	i=i+1

n1=0

for a in range(i):
	n1=n%10
	n=(n-n1)//10
	a=n%10
	if n1>a:
		print('Sim')
		break
	elif n1<=a:
		print('Não')
		break		
	
input()

