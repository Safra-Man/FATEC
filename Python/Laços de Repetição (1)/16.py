#-*- coding:utf-8 -*-

print('****Qual o menor lido?****\n')

n=int(input('Quantidade de Números?: '))
i=0
np=0
m=0

while i<n:
    i=i+1
    print('N%i: '%i)
    np=int(input(' '))
    if i==1:   #Atribui o valor somente para i = 1, pois se zerar o valor de m, nao tera paremetro para comparacao e 0 sera sempre o menor
    	m=np
    else:
    	if np<=m: 
    		m=np
  	
    
print('O menor número é: ',m)

input()

    
