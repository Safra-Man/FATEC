
T=float(input('Trabalho: '))
PR=float(input('Prova Regular: '))

#if 0<T>10 or 0<PR>10:
#	print('Nota Inválida - Digite valores inteiros entre 0 e 10')
#else:		
NF=float((T+PR)/2)
	
if NF>=6:
	print('Aprovado')
elif NF<6 and T<6:
	print('Reprovado')
else:
	print('Substitutiva')

input()
