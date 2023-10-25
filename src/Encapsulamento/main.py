"""
public
protected
private

_, pode ser referenciado como protected, privado/protected (public)
__, pode ser referebciadi como private, (_NOMECLASSE__nomeatributo)

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados
    

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}

        else:

            self.__dados['clientes'].update({id: nome})


    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


# bd = BaseDeDados()
# bd.inserir_cliente(1, 'Guilherme')
# bd.inserir_cliente(2, 'Gomes')
# bd.inserir_cliente(3, 'Santos')
# bd.apaga_cliente(2)
# bd.lista_clientes()

# bd.inserir_cliente(1, "Guilherme")
# bd.inserir_cliente(2, "Gomes")
# bd.inserir_cliente(3, "Santos")
# bd.dados = "Uma outra coisa"
# bd.lista_clientes()

# bd = BaseDeDados()
# bd.inserir_cliente(1, "Guilherme")
# bd.inserir_cliente(2, "Gomes")
# bd._dados = 'Um outro valor qualquer'
# bd.lista_clientes()


bd = BaseDeDados()
bd.inserir_cliente(1, "Gui")
bd.inserir_cliente(2, "Gomes")
# bd.__dados = "Outra Coisa"
bd.dados = "Outro valor"
# print(bd.__dados)
print(bd._BaseDeDados__dados)