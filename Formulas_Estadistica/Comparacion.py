def comparar_menor_que(datos, valor):
    cont = 0
    for item in datos:
        if item < valor:
            cont += 1
    return cont


def comparar_menor_igual_que(datos, valor):
    cont = 0
    for item in datos:
        if item <= valor:
            cont += 1
    return cont


def comparar_mayor_que(datos, valor):
    cont = 0
    for item in datos:
        if item > valor:
            cont += 1
    return cont


def comparar_mayor_igual_que(datos, valor):
    cont = 0
    for item in datos:
        if item >= valor:
            cont += 1
    return cont


def comparar_entre_sin_incluir(datos, valor_peque, valor_grande):
    cont = 0
    for item in datos:
        if valor_peque < item < valor_grande:
            cont += 1
    return cont


def comparar_entre_incluyendo_ambos(datos, valor_peque, valor_grande):
    cont = 0
    for item in datos:
        if valor_peque <= item <= valor_grande:
            cont += 1
    return cont


def comprar_entre_incluyendo_peque(datos, valor_peque, valor_grande):
    cont = 0
    for item in datos:
        if valor_peque <= item < valor_grande:
            cont += 1
    return cont


def comprar_entre_incluyendo_grande(datos, valor_peque, valor_grande):
    cont = 0
    for item in datos:
        if valor_peque < item <= valor_grande:
            cont += 1
    return cont
