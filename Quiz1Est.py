import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
from scipy.stats import kurtosis

dataBase = pd.read_excel("C:/Users/david/Documents/Quiz2Est.xlsx", sheet_name="Hoja1")

dataBase = dataBase["Datos"]


def tabla_de_frecuencia(dataBase):
    n = len(dataBase)
    l = int(round(pow(n, 1 / 2), 0))
    min_val = min(dataBase)
    max_val = max(dataBase)
    tclase = 144

    tabla_frecuencia = pd.DataFrame()

    clasesv = []
    infv = []
    supv = []
    frecuencias = []
    frecuenciarv = []
    inf = min_val
    sup = inf + tclase

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
        sup = inf + tclase

    tabla_frecuencia["Clases"] = clasesv
    tabla_frecuencia["inf"] = infv
    tabla_frecuencia["sup"] = supv
    tabla_frecuencia["Frecuencia"] = frecuencias
    tabla_frecuencia["FrecuenciaR"] = frecuenciarv

    hist = plt.hist(dataBase, bins=l, range=(min_val, max_val))
    plt.xlabel("Clases")
    plt.ylabel("Frecuencia")

    return tabla_frecuencia, hist


tabla = tabla_de_frecuencia(dataBase=dataBase)[0]
hist = tabla_de_frecuencia(dataBase=dataBase)[1]
plt.show()

print(hist)
print(tabla)

caja_bigotes = plt.boxplot(dataBase, vert=False)
plt.show()

q = st.quantiles(dataBase)
q1 = q[0]
q3 = q[2]
rango_intercuartilico = q3 - q1

xbarra = st.mean(dataBase)
desv_est = st.stdev(dataBase)
varianza = desv_est**2


print("x barra", xbarra)
print("")

print(rango_intercuartilico)

print(kurtosis(dataBase))
