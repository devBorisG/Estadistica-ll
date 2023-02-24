# Gráficos de estadística descriptiva

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colormaps
from matplotlib import colors

# %%Gráfico de barras

data = pd.DataFrame({'España': [826, 943, 942, 901],
                     'México': [668, 781, 791, 813],
                     'Colombia': [488, 553, 563, 537]},
                    index=('Lunes', 'Martes', 'Miércoles', 'Jueves'))  # Creación de la base de datos

# %%Diagrama de barras verticales para indicar el número de visitas totales por días de la semana
total = data.sum(axis=1)  # Suma de las filas para estimas las visitas totales por día de la semana
plt.bar(total.index, total)  # Aquí generamos el gráfico de barras para el total de visitas por día
plt.show()  # Mostrar la gráfica

# %%Diagrama de barras horizontales para indicar el número de visitas totales por días de la semana
plt.barh(total.index, total)
plt.show()

# %%Diagrama de barras verticales montadas para indicar las visitas totales y por pais
plt.bar(data.index, data.España + data.México + data.Colombia, label='España')  # Graficamos las barras
plt.bar(data.index, data.México + data.Colombia, label='México')
plt.bar(data.index, data.Colombia, label='Colombia')
plt.legend(loc="best")
plt.show()

# %%Diagrama de barras verticales adyacentes

n = len(data.index)
x = np.arange(n)
width = 0.2
plt.bar(x - width, data.España, width=width, label='España')
plt.bar(x, data.México, width=width, label='México')
plt.bar(x + width, data.Colombia, width=width, label='Colombia')
plt.xticks(x, data.index)
plt.legend(loc="best")
plt.show()

"""
Para ejemplificar la realización de gráficos de torta
vamos a supones que se tienen datos de personas que poseen
cierta cantidad de manzanas

"""

manzanas = [20, 10, 25, 30]
nombres = ['Ana', 'Juan', 'Diana', 'Catalina']

nordata = colors.Normalize(min(manzanas), max(manzanas))
colormap = colormaps["Blues"]
colores = colormap(nordata(manzanas))
desfase = (0, 0, 0, 0.2)

plt.pie(manzanas, labels=nombres, autopct="%0.1f%%", colors=colores, explode=desfase)
plt.axis("equal")
plt.show()
