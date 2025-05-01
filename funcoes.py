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

def remover_dado(dados_rolados, dados_guardados, dado_para_remover):
    remover = dados_guardados[dado_para_remover]
    dados_rolados.append(remover)
    del dados_guardados[dado_para_remover]
    return [dados_rolados, dados_guardados]

def calcula_pontos_regra_simples (face_dados):
    dic = {}
    i = 0
    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0
    soma5 = 0
    soma6 = 0 
    while i < len(face_dados):
        if face_dados[i] == 1:
            soma1 += 1
        if face_dados[i] == 2:
            soma2 += 2
        if face_dados[i] == 3:
            soma3 += 3
        if face_dados[i] == 4:
            soma4 += 4
        if face_dados[i] == 5:
            soma5 += 5
        if face_dados[i] == 6:
            soma6 += 6
        i += 1
    dic[1] = soma1
    dic[2] = soma2
    dic[3] = soma3
    dic[4] = soma4
    dic[5] = soma5
    dic[6] = soma6
    return dic 

def calcula_pontos_soma (valores):
    i = 0
    somat = 0
    while i < len(valores):
        somat += valores[i]
        i+= 1
    return somat 

def calcula_pontos_sequencia_baixa(face_dado):
    presenca = [0, 0, 0, 0, 0, 0]

    i = 0
    while i < len(face_dado):
        valor = face_dado[i]
        if 1 <= valor <= 6:
            presenca[valor - 1] = 1
        i += 1

    j = 0
    while j <= 2: 
        if presenca[j] == 1 and presenca[j+1] == 1 and presenca[j+2] == 1 and presenca[j+3] == 1:
            return 15
        j += 1

    return 0

def calcula_pontos_sequencia_alta(face_dado):
    presenca = [0, 0, 0, 0, 0, 0]

    for valor in face_dado:
        if 1 <= valor <= 6:
            presenca[valor - 1] = 1

    for i in range(2):  
        if presenca[i] and presenca[i+1] and presenca[i+2] and presenca[i+3] and presenca[i+4]:
            return 30

    return 0 

def calcula_pontos_full_house(face_dado):
    i = 0
    lista1 = []
    lista2 = []

    while i < len(face_dado):
        if len(lista1) == 0:
            lista1.append(face_dado[i])
        elif face_dado[i] == lista1[0]:
            lista1.append(face_dado[i])
        elif len(lista2) == 0:
            lista2.append(face_dado[i])
        elif face_dado[i] == lista2[0]:
            lista2.append(face_dado[i])
        i += 1

    if (len(lista1) == 3 and len(lista2) == 2) or (len(lista1) == 2 and len(lista2) == 3):
        return face_dado[0] + face_dado[1] + face_dado[2] + face_dado[3] + face_dado[4]
    else: 
        return 0 
    
def calcula_pontos_quadra(face_dado):
    i = 0
    while i < len(face_dado):
        valor = face_dado[i]
        lista = [valor]

        j = i + 1
        while j < len(face_dado):
            if face_dado[j] == valor:
                lista.append(valor)
            j += 1

        if len(lista) >= 4:
            total = 0
            z = 0
            while z < len(face_dado):
                total += face_dado[z]
                z += 1
            return total  

        i += 1
    return 0

def calcula_pontos_quina(face_dado):
    i = 0
    while i < len(face_dado):
        valor = face_dado[i]
        cont = 0
        j = 0
        while j < len(face_dado):
            if face_dado[j] == valor:
                cont += 1
            j += 1
        if cont >= 5:
            return 50
        i += 1
    return 0

def calcula_pontos_regra_avancada (face_dado_5):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(face_dado_5)
    dic['full_house'] = calcula_pontos_full_house(face_dado_5)
    dic['quadra'] = calcula_pontos_quadra(face_dado_5)
    dic ['sem_combinacao'] = calcula_pontos_soma (face_dado_5)
    dic ['sequencia_alta'] = calcula_pontos_sequencia_alta(face_dado_5)
    dic ['sequencia_baixa'] = calcula_pontos_sequencia_baixa (face_dado_5)
    return dic 
