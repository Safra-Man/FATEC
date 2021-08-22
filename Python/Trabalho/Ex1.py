

#Exercicio de Python para o dia 27

#*-* coding utf-8 *-*


a=float(input('Alimentação: '))
h=float(input('Higiene: '))
l=float(input('Limpeza: '))

a=a*0.9
h=h*0.85
l=l*0.8

print('----------')
print('Alimentação: R$ %1.2f'%a)
print('Higiene: R$ %1.2f'%h)
print('Limpeza: R$ %1.2f'%l)

input()