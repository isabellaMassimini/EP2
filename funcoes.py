import random
def rolar_dados (numero):
    dados = []
    i =0
    while i < numero:
        dado = random.randint(1, 6)
        dados.append(dado)
        i += 1
    return dados
