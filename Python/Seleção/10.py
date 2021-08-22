#-*- coding:utf-8 -*-

print('****Qual data vem primeiro?****')

dia=int(input('Dia(xx): '))
mes=int(input('Mes(xx): '))
ano=int(input('Ano(xxxx): '))

dia1=int(input('2º Dia(xx): '))
mes1=int(input('2º Mes(xx): '))
ano1=int(input('2º Ano(xxxx): '))

if ano1<ano:
    print(' A data que vem primeiro é %i'%dia1,'/ %2i'%mes1,'/ %i'%ano1)
elif ano<ano1:
    print(' A data que vem primeiro é %i'%dia,'/ %2i'%mes,'/ %i'%ano)
elif ano==ano1 and mes1<mes:
    print(' A data que vem primeiro é %i'%dia1,'/ %2i'%mes1,'/ %i'%ano1)
elif ano==ano1 and mes<mes1:
    print(' A data que vem primeiro é %i'%dia,'/ %2i'%mes,'/ %i'%ano)
elif ano==ano1 and mes==mes1 and dia<dia1:
    print(' A data que vem primeiro é %i'%dia,'/ %2i'%mes,'/ %i'%ano)
elif ano==ano1 and mes==mes1 and dia1<dia: 
    print(' A data que vem primeiro é %i'%dia1,'/ %2i'%mes1,'/ %i'%ano1)
else:
    print('As datas são iguais!')

input()