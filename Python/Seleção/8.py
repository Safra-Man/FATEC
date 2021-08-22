#-*- coding:utf-8 -*-

print('****Verifica se é Triângulo****')

#A<B<C -->> Ordem! Fica mais fácil analisar se colocar em ordem!

a=int(input('Lado A: '))
b=int(input('Lado B: '))
c=int(input('Lado C: '))
n=0

#Para construir um triângulo é necessário que a medida de qualquer um dos lados 
#seja menor que a soma das medidas dos outros dois e maior que o valor absoluto 
#da diferença entre essas medidas.

if a>b and a>c: # Se A for o maior de todos
    n=c
    c=a
    a=n
elif b>a and b>c: # Se B for o maior de todos
    n=c
    c=b
    b=n
elif b<a: # Se B for menor que A
    n=a
    a=b
    b=n

print(a,b,c)

if c<(a+b) and c>(b-a):
    print('Formam um Triângulo!')
else:
    print('Não formam um Triângulo')

input()


