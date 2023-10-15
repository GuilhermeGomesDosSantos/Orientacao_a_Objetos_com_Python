# class Pessoa:
#     pass

# class Pessoa:
#     def falar(self):
#         print('Pessoa está falando...')

from datetime import datetime

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # variavel = 'Valor'
        # print(variavel)

    # def outro_metodo (self):
    #     print(self.nome)

    def falar (self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        
        print (f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar (self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer (self, alimento):

        if self.comendo:
            print(f'{self.nome} já está Comendo.')
            return
        
        elif self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        

        print(f'{self.nome} está Comendo {alimento}')
        self.comendo = True

    def parar_comer (self):

        if not self.comendo:
            print (f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de Comer')
        self.comendo = False

    def get_ano_nascimento (self):
        return self.ano_atual - self.idade