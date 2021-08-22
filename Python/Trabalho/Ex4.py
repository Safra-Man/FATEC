#*-* coding:utf-8 *-*

n=int(input('n: '))
s=0
s=s+1*(n%2)
i=0

while n>0:
	n=n//10
	s=s+1*(n%2)
	i=i+1
s=i-s
print('Dígitos pares:',s)






