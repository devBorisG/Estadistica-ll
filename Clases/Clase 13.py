"""
X_barra = media de poblacion 1
Y_barra = media poblacion 2 TODO: cambiar miu por Y_barra
delta_sub_0 = 0
"""
import math

import numpy as np
import pandas as pd
from scipy.stats import t,norm

df = pd.read_excel("/home/david/Documentos/Datos2poblacionesMuestrapequeña.xlsx", sheet_name="Hoja1")

n = len(df["Xbienrecordado"])
m = len(df["Ymalrecordado"])
x_barra = df["Xbienrecordado"].mean()
y_barra = df["Ymalrecordado"].mean()
s12 = df["Xbienrecordado"].var()
s22 = df["Ymalrecordado"].var()

t_calc = (x_barra - y_barra) / (np.sqrt((s12 / n) + (s22 / m)))

# Estimación de los grados de libertad
nu = ((s12 / n) + (s22 / m)) ** 2 // (((s12 / n) ** 2 / (n - 1)) + ((s22 / m) ** 2 / (m - 1)))
nu = math.floor(nu)

# t Critico a un valor alfa de 0.05
alfa = 0.05
tcritico = -t.ppf(0.05, nu)

# Conclusión
if t_calc >= tcritico:
    print("Se rechaza Ho, es decir, los anuncios bien recordados tienen mayor actividad cerebral que los anuncios "
          "recordados")
else:
    print("NO se rechaza Ho, es decir, los anuncios bien recordados tiene la misma actividad qcerebral que los "
          "anuncios no recordados")

#%% Ejercicio de las leyes aburridas

p1m = 0.875
q1m = 1-p1m
m = 191
x = 101

p2m = 0.529
q2m = 1-p2m
n = 65
y = 56

p_gorro = (m/(m+n))*p1m+(n/(m+n))*p2m
q_gorro = 1-p_gorro
z = (p1m-p2m)/(np.sqrt(p_gorro*q_gorro*((1/m)+(1/n))))

# Prueba de hipótesis con valores P
p=2*(1-norm.cdf(z))

alfa = 0.05

# Conclusion
if p <= alfa:
    print("Se rechaza Ho, es decir, la probabilidad de declararse culpable e ur a prision es diferente que declararse inocente e ir a prision")
else:
    print("No se rechaza Ho, es decir, la probabilidad de declararse culplable e ir a prision es la misma que declararse inocente e ir a prision")