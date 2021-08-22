#-*- coding:utf-8 -*-

print('****Fórmula de Bhaskara****')

a=float(input('Digite A: '))
b=float(input('Digite B: '))
c=float(input('Digite C: '))

delta=(b**2)-(4*a*c)

print('Delta: ',delta)

if delta<0:
    print('Não existem Raízes Reais!')
    b=-b
    delta=-delta
    i=delta**0.5/(2*a)
    x=b/(2*a)

    if i<0:
        print('As Raízes são x1: %1.2f'%x,'+%1.2fi'%-i,' e x2: %1.2f'%x,'%1.2fi'%i)    
        input()
    else:
        print('As Raízes são x1: %1.2f'%x,'+%1.2fi'%i,' e x2: %1.2f'%x,'-%1.2fi'%i)    
        input()

else:
    b=-b
    delta=delta**0.5
    x1=(b+delta)/(2*a)
    x2=(b-delta)/(2*a)

    print('Raiz x1: ',x1)
    print('Raiz x2: ',x2)
    input()