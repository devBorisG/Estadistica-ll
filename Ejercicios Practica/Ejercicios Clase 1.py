import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps
from matplotlib import colors

# %%Ejercicio 1: Defectos en vehículos
frecuencia = [30, 21, 6, 6, 5, 5, 4, 4]
tipoDefecto = ['Fuera de perfil',
               'Piezas desordenadas',
               'Agujero',
               'Fuera de secuencia',
               'Partes no lubricadas',
               'Piezas con rebabas',
               'Abolladura',
               'Otras']

# Diagrama de barras verticales
plt.bar(tipoDefecto, frecuencia)
plt.show()

# Diagrama de barras horizontal
plt.barh(tipoDefecto, frecuencia)
plt.show()

# Diagrama de torta
plt.pie(frecuencia, labels=tipoDefecto, autopct="%0.1f%%")
plt.axis("equal")
plt.show()
