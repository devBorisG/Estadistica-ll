#Graficos de estadistica descriptivas

#%%Gráfico de barras
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'España': [826, 943, 942, 901],
                    'México': [668, 781, 791, 813],
                    'Colombia': [488, 553, 563, 537]},
                    index=('Lunes','Martes','Miercoles','Jueves')) #Creación de la base de datos

#%%Diagrama de barras verticales para indicar el número de visitas totales por dias de la semana
total = data.sum(axis=1)    #Suma de las filas para estimas las visitas totales por día de la semana
plt.bar(total.index, total) # Aqui generamos el gráfico de barras para el total de visitas por día
plt.show()                  #Mostrar la gráfica

#%%Diagrama de barras horizontales para indicar el número de visitas totales por dias de la semana
plt.barh(total.index, total)
plt.show()

#%%Diagrama de barras verticales montadas para indicar las visitas totales y por pais
plt.bar(data.index, data.España + data.México + data.Colombia, label='España') #Graficamos las barras
plt.bar(data.index, data.México + data.Colombia, label='México')
plt.bar(data.index, data.Colombia, label='Colombia')
plt.legend(loc="best")
plt.show()

#%%Diagrama de barras verticales adyacentes
import numpy as np

n=len(data.index)
x=np.arange(n)
width=0.2
plt.bar(x-width, data.España, width=width, label='España')
plt.bar(x, data.México, width=width, label='México')
plt.bar(x+width, data.Colombia, width=width, label='Colombia')
plt.xticks(x,data.index)
plt.legend(loc="best")
plt.show()

"""
Para ejemplificar la realizacion de gráficos de torta
vamos a supones que se tienen datos de personas que poseen
cierta cantidad de manzanas

"""

from matplotlib import cm
from matplotlib import colors

manzanas = [20,10,25,30]
nombres = ['Ana','Juan','Diana','Catalina']

normdata = colors.Normalize(min(manzanas),max(manzanas))
colormap = cm.get_cmap("Blues")
colores = colormap(normdata(manzanas))
desfase = (0,0,0,0.2)

plt.pie(manzanas, labels=nombres, autopct="%0.1f%%", colors=colores,explode=desfase)
plt.axis("equal")
plt.show()