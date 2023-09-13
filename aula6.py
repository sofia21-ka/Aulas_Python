'''
compraC = True
dadosc = 'Compra no valor de R$12.50 e entrega confirmada'

for i in range(3):
    if compraC:
        print(dadosc)
        print('detalhes enviados para seu email')
        break
else:
    print('falha na compra')
'''

#For loop - Nested Loops (Laços alinhados)
#outer loop (laço externo)
# inner loop (loop interno)
'''
for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero1,[numero2])
'''

'''
for numero1 in range(1,6):
    print('produto'+ str(numero1))
    for numero2 in range(5):
        print(numero1,[numero2])
    '''
'''
palavra = 'FANTASTICO'
for space in palavra:
    print(space) #ir reto
    # print(space, end = ' ') # ter espaço
    ''' 
'''
******
******
******
******
******
******
'''

linha = 6
coluna = 6
simbolo = '*'
for l in range(linha):
    for c in range(coluna):
        print(simbolo, end =' ')
