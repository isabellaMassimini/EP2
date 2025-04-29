import random
def rolar_dados (numero):
    dados = []
    i =0
    while i < numero:
        dado = random.randint(1, 6)
        dados.append(dado)
        i += 1
    return dados

def guardar_dado (dados_rolados, dados_guardados, dado_armazenado):
    tirar = dados_rolados[dado_armazenado]
    dados_guardados.append(tirar)
    del dados_rolados[dado_armazenado]
    dados_no_estoque = [dados_rolados, dados_guardados]
    return dados_no_estoque