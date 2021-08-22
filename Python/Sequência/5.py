n=int(input('n: '))
a=n
b=n
a=(n//100)-(n//10000)
b=((n/100)-a)*100
n=a+b
print('%1.0f'%n)
