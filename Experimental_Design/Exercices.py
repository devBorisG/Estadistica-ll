import Completely_Random
import pandas as pd
from itertools import combinations
from scipy.stats import t, f, shapiro, bartlett
import matplotlib.pyplot as plt
import numpy as np


"""
The metodo_lsd_dca function takes the dataframe and calculates the L.S.D method for DCA.
    It returns a table with the pairs of means, their difference and if they are significant or not.

:param self: Represent the instance of the class
:return: A table with the results of the l.s.d method
:doc-author: David
"""
medias = [135.435,147.988333,147.686667]  # Volvemos la columna de medias de la tabla de datos una lista
comb = combinations(medias, 2)
tabla_lsd = pd.DataFrame()  # Aquí consignamos los resultados del método LSD
parejas = []
diferencia = []
conclusion = []
t_alfa = -t.ppf(0.05, 18 - 2)
lsd = t_alfa * np.sqrt(0.07897778 * ((1 / 3) + (1 / 2)))
for row in list(comb):
    parejas.append(row)
    diferencia.append(abs(row[0] - row[1]))
    if abs(row[0] - row[1]) >= lsd:
        conclusion.append("Significativa")
    else:
        conclusion.append("No significativa")
tabla_lsd["Parejas"] = parejas
tabla_lsd["Diferencia"] = diferencia
tabla_lsd["Conclusión"] = conclusion

    # Gráficos de medias
intervalo_c = t_alfa * np.sqrt(0.07897778 / (18 / 2))
for i in range(2):
    media = medias[i]
    i_sup = media + intervalo_c
    i_inf = media - intervalo_c
    plt.plot([i, i, i], [i_inf, media, i_sup], linewidth=2, marker=".", color="black")
plt.xlabel("Tratamientos")
plt.ylabel("Tiempo de ensamble [min]")
plt.show()
