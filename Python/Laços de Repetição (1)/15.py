#-*- coding:utf-8 -*-

print('****Maior Quadrado Perfeito antes de N**** \n')

n=int(input('Digite N: '))
i=0
n2=0

while n2<=n:
    i=i+1
    n2=i*i


    
if n<n2:
	print("\n O menor quadrado perfeito antes de N é: ",(i-1)*(i-1))
else:   
	print("\n O menor quadrado perfeito antes de N é: ",i*i)

input()


