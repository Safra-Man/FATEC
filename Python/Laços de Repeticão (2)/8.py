#-*- coding:utf-8 -*-

print('****Converte para Binário!****\n')

n=int(input('Digite o Valor Converter: '))
sobra=n
aproximacao=1
binario=1
exponencial=0

while sobra>0:
	if(sobra//aproximacao)<1:
		aproximacao=aproximacao//2
		divisor=aproximacao		
		while divisor!=1:
			exponencial=exponencial+1
			divisor=divisor//2

	binario=10**exponencial
	sobra=sobra-aproximacao
	aproximacao=1
aproximacao=aproximacao*2

print(binario)
input()


***************************************

algoritimo() {
        let n = 542;
        let sobra = n;
        let aproximacao = 1;
        let binario = 0;
        let exponencial = 0;
        while(sobra > 0) {
            if((sobra / (aproximacao * 2)) < 1) {
                binario += 10**exponencial;
                sobra -= aproximacao;
                aproximacao = 1;
                exponencial = 0;
                continue;
            }
            exponencial++;
            aproximacao *= 2;
        }
        return binario;
    }

#algoritimo() {
#        let n = 542;
#        let sobra = n;
#        let aproximacao = 1;
#        let binario = 0;
#        while(sobra > 0) {
#            if((sobra / aproximacao) < 1) {
#                aproximacao /= 2;
#                let divisor = aproximacao;
#                let exponencial = 0;
#                while(divisor != 1) {
#                    exponencial++;
#                    divisor /= 2;
#                }
#                binario += 10**exponencial;
#                sobra -= aproximacao;
#                aproximacao = 1;
#                continue;
#            }
#            aproximacao *= 2;
#        }
#        return binario;
#    }





#q=n
#r=0

#while q!=0:
#	r=q%2
#	n=q//2				Versão que não Inverte o Resto
#	q=n
#	print(r%2,end="")
	
		
#input()

