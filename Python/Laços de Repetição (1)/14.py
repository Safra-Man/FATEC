#-*- coding:utf-8 -*-

print('****Número de Vogais, prima ! para sair**** \n')
letra="a"
n=0

while letra!="!":
    letra=str(input('Letra: '))
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    	n=n+1
    
print("\n A quantidade de vogais é de: ",n)
input()


