#-*- coding:utf-8 -*-

print('****Qual o dia da semana?****')

#Domingo é 1

d=int(input('Digite Dia>0: '))

if d==0:
    print('Dia Inválido!')
elif (d-2)%7==0:
    print('Segunda-Feira')
elif (d-3)%7==0:
    print('Terça-Feira')
elif (d-4)%7==0:
    print('Quarta-Feira')
elif (d-5)%7==0:
    print('Quinta-Feira')
elif (d-6)%7==0:
    print('Sexta-Feira')
elif (d-7)%7==0:
    print('Sábado')
else:
    print('Domingo')

input()

#Dia=7*nº da Semana + Dia Da semana de 1 a 7