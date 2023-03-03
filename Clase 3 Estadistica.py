import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter
import statistics as st

# %%Diagrama de pareto

# Create DataFrame
df = pd.DataFrame({'Frecuencia': [4, 6, 30, 6, 4, 5, 5, 21]})
df.index = ["Abolladuras", "Agujeros", "Fuera de Perfil",
            "Fuera de Secuencia", "Otros", "Partes no Lubricadas",
            "Piezas con Rebabas", "Piezas Desordenadas"]

# Organizar los datos de orden descendente
df = df.sort_values(by="Frecuencia", ascending=False)  # Esta función organiza los datos de la columna Frecuencia de
# mayor a menor

# Añadir una columna para mostrar el porcentaje acumulado
df['F.R Acumulada'] = df['Frecuencia'].cumsum() / df['Frecuencia'].sum() * 100

# Definir las estéticas para el gráfico
color1 = "steelblue"
color2 = "red"
line_size = 4

# Crear gráfico de barras básico
fig, ax = plt.subplots()
ax.bar(df.index, df["Frecuencia"], color=color1)

# Añadir gráfico lineal de porcentaje acumulado
ax2 = ax.twinx()
ax2.plot(df.index, df['F.R Acumulada'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter)

# Colores ejes
ax.tick_params(axis='y', color=color1)
ax2.tick_params(axis='y', color=color2)

plt.show()

# %%Tabla de frecuencia para histograma

dataBase = pd.read_excel("C:/Users/david/Estadistica.xlsx", sheet_name="Clase  1 - Cuantitativo Histogr")

# Parámetros para la construcción de la tabla de frecuencia
dataBase = dataBase["datos"]


def tabla_de_frecuencia(dataBase):
    n = len(dataBase)
    l = int(round(pow(n, 1 / 2), 0))
    min_val = min(dataBase)
    max_val = max(dataBase)
    tclase = (max_val - min_val) / l

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

# %%Diagrama de caja

caja_bigotes = plt.boxplot(dataBase, vert=False)
plt.show()

# %%Estadística descriptiva numérica

xbarra = st.mean(dataBase)
desv_est = st.stdev(dataBase)
varianza = desv_est**2
q = st.quantiles(dataBase)
q1 = q[0]
q3 = q[2]
rango_intercuartilico = q3 - q1

print(q1)
print(q3)
print(rango_intercuartilico)
