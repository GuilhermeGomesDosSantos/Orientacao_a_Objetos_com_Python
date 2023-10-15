from datetime import datetime

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

# p1 = Pessoa('Gui', 20)
# p1.get_ano_nascimento()
# print(p1.idade)
# p1.get_ano_nascimento()

# p1 = Pessoa.por_ano_nascimento('Gui', 20)
# print(p1.idade)
# p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Gui', 2003)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()