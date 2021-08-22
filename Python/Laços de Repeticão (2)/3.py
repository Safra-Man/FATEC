#-*- coding:utf-8 -*-

print('****Soma letras que estão em Ordem****\n')

# tá foda, vou pular

soma=1
lant=str(input('Digite:'))

while True:
	l=str(input('Digite:'))
	if l>lant:
		soma=soma+1
		lant=l
	else:
		break
print(soma)


input()

