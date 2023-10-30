from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Gui')

caneta = Caneta('Bic')

maquina = MaquinaDeEscrever()
# print(escritor.nome)
# print(caneta.marca)


# escritor.ferramenta = caneta
# escritor.ferramenta.escrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

# escritor.ferramenta = caneta
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()