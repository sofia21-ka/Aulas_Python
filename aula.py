'''
print("oi")
ano_nasc= 1985
idade = 2023 - ano_nasc
print("Voce tem ",idade," anos")

ano = int(input("Qual o ano que voce nasceu? "))
id= 2023 - ano
print("Voce tem ",id,"anos \n \n")

nome = 'Kemily'
sob = 'Neponoceno'
prof = 'herdeira'
texto = f'A  {nome} e um excelente [{ prof}] '
t1 = 'A' + nome + sob + 'eh uma excelente' + prof
print(texto)
print("Aqui eh com a junção de strings: ",t1)
cal= 2**(3+4)
print(cal)

 '''

 #Desafio1 = Imprimir 'Ola mundo'
print("\t Desafio 1 \n")
print("Olá Mundo! \n")


#Desafio2 -> Declarar 2var(idade e nome) sendo int e str. Após isso, imprimir na tela 'Ola me chamo ... e eu tenho ... anos. 
print("\t Desafio 2\n")
nome = input("Informe nome: ")
id = int(input("Informe idade: "))
print("Olá! Me chamo ",nome,"e eu tenho ",id," anos.\n")


''' Tipos de  chamar o  '.format'
texto = f'Ola! Me chamo {nome} e eu tenho {id} anos. '
print(texto)
print("Meu nome eh {} e eu tenho {} anos".format(nome,id))
t= "Meu nome eh {} e eu tenho {} anos".format(nome,id)
print(t)
'''