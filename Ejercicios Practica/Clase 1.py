import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps
from matplotlib import colors

# %%Ejercicio 1: Defectos en vehículos
data = pd.DataFrame({'Fuera de perfil': [30, 37.037, 37.07],
                     'Piezas desordenadas': [21, 25.926, 62.963],
                     'Agujero': [6, 7.407, 70.370],
                     'Fuera de secuencia': [6, 7.407, 77.778],
                     'Partes no lubricadas': [5, 6.173, 83.951],
                     'Piezas con rebabas': [5, 6.173, 90.123],
                     'Abolladura': [4, 4.938, 100.000]},
                    index=('Frecuencia', 'F. Relativa', 'F.R. Acumulada'))

# Diagrama de barras verticales:
total = data.sum(axis=1)  # Suma de frecuencia de errores
plt.bar(total.index, total)  # Aquí se genera el gráfico de barras
plt.show()  # Mostrar gráfica

# Diagrama de barras horizontales:
plt.barh(total.index, total)
plt.show()
data.
# Diagrama de torta:
nombres = [label for label in data.items()]
nordata = colors.Normalize(min(data.iloc[1]), max(data.iloc[1]))
colormap = colormaps["Greens"]
colores = colormap(nordata(data.iloc[1]))
desfase = (0, 0, 0, 0, 0, 0, 0.2)

print(nombres)
plt.pie(data.iloc[1],
        labels=data.iloc[0],
        autopct="%0.1f%%")
plt.axis("equal")
plt.show()

# %%Ejercicio 2: