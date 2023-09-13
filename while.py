#while é loop infinito até sua condição ser atingida
'''
valor =100
dia =1 
while valor>20:
    print('DIA',dia,' DA PROMOÇÃO!!')
    dia+=1
    print(f'HOJE ESTA A ${valor}')

    valor -= 5

#oPERADORES TERNARIOS
id = int(input("informe idade: "))
#if id>= 13:
   # resultado = print("Voto nao permitido")
#else:
#    resultado = print('voto permitido')

resultado = 'voto permitido' if id>=16 else 'voto nao permitido'
print("\n",resultado)

'''

#valor com comissao de 10%
valor = int(input("Informe valor: "))
while valor>20:
    valor = (valor*0.10)+ valor
    print(f'o valor final eh de R${valor}')
    break