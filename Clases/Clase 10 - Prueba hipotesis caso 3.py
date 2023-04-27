import pandas as pd
from scipy.stats import t, norm
import statistics as st
from math import sqrt


df = pd.read_excel("C:/Users/david/Documents/clasehoy.xlsx", sheet_name="Hoja1")

# 1. identificar el parametro de interes: Media caso 3
## Prueba de hipotesis para la media
## Hipotesis nula
miu = 10
alfa = 0.05
x_barra = st.mean(df["Datos"])
s = st.stdev(df["Datos"])
n = len(df["Datos"])

t_calc = (x_barra-miu)/(s/sqrt(n))
t_critica = -t.ppf(alfa, n-1)# porque necesitamos la parte derecha

if t_calc > t_critica:
    print("Se rechaza Ho a favor de Ha")
else:
    print("No se rechaza Ho")

# Prueba de hipotesis con valores P
miu = 245
alfa = 0.01
x_barra = 246.19
s = 3.60
n = 50

z_calculada = (x_barra-miu)/(s/sqrt(n))
fi_z_calculada = norm.cdf(z_calculada)
p = 2*(1-fi_z_calculada)

if p > alfa:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho a favor de Ha")

