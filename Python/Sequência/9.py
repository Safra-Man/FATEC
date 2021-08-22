c=int(input('Caminhada: '))
o=int(input('Ônibus: '))
m=int(input('Metrô: '))

h=(c+o+m)/60
mi=c+o+m
s=(c+o+m)*60

print('Horas: %1.2f hrs'%h)
print('Minutos:',mi)
print('Segundos:',s)
