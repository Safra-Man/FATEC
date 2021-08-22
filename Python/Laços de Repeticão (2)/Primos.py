#-*- coding:utf-8 -*-
import math
print('****Exibe primos****\n')

n=int(input('Digite N valores para validar: '))
i=0
for i in range(1,n):
	c1=((i**(2*i))^3)
	c2=((26*math.e)//i)+1
	if c1%26==c2%26:
		print(i)


input()

math.e
