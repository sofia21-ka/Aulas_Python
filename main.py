#dife  função
def somar(valor1,valor2):
    soma = valor1*valor2
    return soma

#chama função

resp = somar(3,4)
print(f' valor e {resp}')

#declarando Função
def imprime_msg(nomePes):
    print(f' o usuario {nomePes} escreveu uma mensagem')

#chamando a funçaõ
nome = input('Digite nome ')
imprime_msg(nome)