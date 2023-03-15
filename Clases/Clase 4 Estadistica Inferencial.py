import math
import sympy as sp
from scipy.stats import norm
from scipy.stats import chi2
import matplotlib.pyplot as plt

# %% Ejercicio 1
"""Definicion de parametros"""
xbarra = 3.5
n = 30

# Definición, creación y solución de la integral definida
x = sp.Symbol('x')
y1 = (3 / 125) * x ** 3
y2 = (3 / 125) * x ** 4
miu = sp.integrate(y1, (x, 0, 5))
ex2 = sp.integrate(y2, (x, 0, 5))

# Calculos para hallar probabilidad
vx = ex2 - (miu ** 2)
sigma = pow(vx, 1 / 2)

z = (xbarra - miu) / (sigma / math.sqrt(n))
fiz = norm.pdf(float(z), 0, 1)

print("La probabilidad que el tiempo excedido sea mejor a 3.5min es:" + str(fiz))

# %% Ejercicio 2
n = 20
s2 = 7
sigma2 = 7.5

chi2_cal = ((n-1)*s2)/sigma2
fichi = chi2.pdf(chi2_cal, n-1)

print("La probabilidad que la varianza sea menor a 7 es:", fichi)

# Curva de chi^2
r = chi2.rvs(7.5, 0, 1, 100)
plt.hist(r)
