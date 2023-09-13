'''frut_user = input("Informe frutas e separe com virgula: ")
frut_list = frut_user.split(',')
print(frut_list)'''

#calsses construtoras e sempre que iniciar a class, tem que ser com letra maiuscula

'''class Funcionarios:
    nome = 'Elena'
    sobN = "Cabral"

user1 = Funcionarios()

print(user1.nome)
print(user1.sobN)'''
#criar modulo
from datetime import datetime
#criar classe
class Func:
    def __init__(self,nome,sobrN,dataN): #desse jeito diminuo o cod 
        self.nome = nome 
        self.sobrN = sobrN
        self.dataN = dataN
    def nome_comp(self):
        return self.nome +' '+ self.sobrN
    def id_fun(self):
        anoAtual = datetime.now().year
        self.dataN = int(anoAtual - self.dataN)
        return self.dataN

user1 = Func('elena','Cabral',2000)
print('com print:',user1.nome, user1.sobrN,user1.dataN)
print(user1.nome_comp())
print(Func.id_fun(user1))
#criar parametros
#user1.nome = 'elena'
#user1.sobrN ='Cabral'
#user1.dataN = '12/01/2009'
#print
