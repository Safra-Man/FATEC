#-*- coding:utf-8 -*-

n=int(input('n: '))

a=n
b=n

a=n//100
b=int(round(((n/100)-a),2)*100)


s=a+b
c=s*s

if c==n:
    print('Sim')
else:
    print('Não')




#*>>> a=13.946
#>>> print(a)
#13.946
#>>> print("%.2f" % a)
#13.95
#>>> round(a,2)
#13.949999999999999
#>>> print("%.2f" % round(a,2))
#13.95
#>>> print("{0:.2f}".format(a))
#13.95
#>>> print("{0:.2f}".format(round(a,2)))
#13.95
#>>> print("{0:.15f}".format(round(a,2)))
#13.949999999999999
