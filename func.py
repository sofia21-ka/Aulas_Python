#armazenar mais de uma função em variaveis
#manter a sequencia dos dados em uma variavel
# O lower() metodo retorna uma string onde todos os caracteres são minúsculos. 
#Simbolo e numeros sao ignorados

cor_cliente = input("Digite a cor desejada: ")
cores = ['amarelo','azul','verde','vermelho']

if cor_cliente.lower() in cores:
    print("sim")
else:
    print("Nao temos essa cor em estoque")
