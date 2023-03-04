import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

# %%Tabla de frecuencia para histograma

data_base = pd.read_excel("C:/Users/david/Documents/quiz1.xlsx", sheet_name="Hoja1")

data_base = data_base["Datos"]


def tabla_de_frecuencia(data_base):
    n = len(data_base)
    l = 6
    print(l)
    min_val = min(data_base)
    max_val = max(data_base)
    t_clase = (max_val - min_val) / l
    print(t_clase)
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
        for element in data_base:
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

    hist = plt.hist(data_base, bins=l, range=(min_val, max_val), color="green", ec="black")
    plt.xlabel("Clases")
    plt.ylabel("Frecuencia")

    return tabla_frecuencia, hist


tabla = tabla_de_frecuencia(data_base=data_base)[0]
hist = tabla_de_frecuencia(data_base=data_base)[1]
plt.show()

# %%Diagrama de caja

caja_bigotes = plt.boxplot(data_base, vert=False)
plt.show()

xbarra = st.mean(data_base) # media
mediana = st.median(data_base)

desv_est = st.stdev(data_base)
varianza = desv_est**2
q = st.quantiles(data_base)
q1 = q[0]
q2 = q[1]
q3 = q[2]
q4 = q[3]
rango_intercuartilico = q3 - q1
