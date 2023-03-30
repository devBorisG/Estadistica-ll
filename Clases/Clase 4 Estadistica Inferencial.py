import math
import sympy as sp
from scipy.stats import norm
from scipy.stats import chi2
import matplotlib.pyplot as plt
import Formulas_Estadistica.Teoremas as teorema

# %% Ejercicio 1
"""Definicion de parametros"""
xbarra = 0.5
n = 50

# Definición, creación y solución de la integral definida
x = sp.Symbol('x')
y1 = ((3/2)*(1-x**2)) * x
y2 = ((3/2)*(1-x**2)) * x ** 2
miu = sp.integrate(y1, (x, 0, 1))
ex2 = sp.integrate(y2, (x, 0, 1))

# Calculos para hallar probabilidad
vx = ex2 - (miu ** 2)
sigma = pow(vx, 1 / 2)

z = teorema.teorema_limite_central(xbarra, miu, sigma, n)
fiz = teorema.probabilidad_z(z)  # Para hallar z se usa cdf, para hallar P se usa ppf

print("La probabilidad que la carga sea menor a 0.5 toneladas es:" + str(1-fiz)) # Como me estan preguntando por mayor le tengo que restar 1



# %% Ejercicio 2
n = 20
s2 = 7
sigma2 = 7.5

chi2_cal = teorema.teorema_varianza(n, s2, sigma2)
fichi = teorema.probabilidad_chi2(chi2_cal, n)

print("La probabilidad que la varianza sea menor a 7 es:", fichi)

# Curva de chi^2
r = chi2.rvs(7.5, 0, 1, 100)
plt.hist(r)

#Se usa teorema
