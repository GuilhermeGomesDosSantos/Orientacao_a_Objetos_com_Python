from datetime import datetime
from random import randint
class Pessoa:
    anoAtual = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento (self):
        print(self.anoAtual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.anoAtual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gerar_id():
        rand = randint(1000, 19999)
        return rand
    
p1 = Pessoa('Gui', 20)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gerar_id())
print(p1.gerar_id())