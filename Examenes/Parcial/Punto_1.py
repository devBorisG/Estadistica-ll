import pandas as pd
import matplotlib.pyplot as plt

def tabla_de_frecuencia(dataBase):
    n = len(dataBase)
    l = int(round(pow(n, 1 / 2), 0))
    min_val = min(dataBase)
    max_val = max(dataBase)
    t_clase = (max_val - min_val) / l
    print((max_val - min_val)/154.0988)
    tabla_frecuencia = pd.DataFrame()

    clasesv = []
    infv = []
    supv = []
    frecuencias = []
    frecuenciarv = []
    inf = min_val
    sup = inf + t_clase

    for i in range(l):
        clasesv.append(i)
        count = 0
        for element in dataBase:
            if inf <= element < sup + 0.0001:
                count += 1
        frecuencias.append(count)
        frecuenciar = count / n
        frecuenciarv.append(frecuenciar)
        infv.append(inf)
        supv.append(sup)
        inf = sup
        sup = inf + t_clase

    tabla_frecuencia["Clases"] = clasesv
    tabla_frecuencia["inf"] = infv
    tabla_frecuencia["sup"] = supv
    tabla_frecuencia["Frecuencia"] = frecuencias
    tabla_frecuencia["FrecuenciaR"] = frecuenciarv

    hist = plt.hist(dataBase, bins=l, range=(min_val, max_val))
    plt.xlabel("Clases")
    plt.ylabel("Frecuencia")

    return tabla_frecuencia, hist


data_base = pd.read_excel("C:/Users/david/Documents/ParcialEst.xlsx", sheet_name='Punto1')
data_base = data_base["Datos"]
tabla = tabla_de_frecuencia(data_base)[0]
