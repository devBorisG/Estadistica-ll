"""
Prueba de hipotesis para la proporcion
"""

# Ejemplo 1

from scipy.stats import norm
from math import sqrt

# 1. Definir P0
p_0 = 1.5*0.2
p_gorro = 1276/4115
n = 4115
z = (p_gorro-p_0)/sqrt((p_0*(1-p_0))/n)

# Prueba de hipotesis con valores P
fi_z = norm.cdf(z)
p = 1-fi_z
alfa = 0.1

if p > alfa:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho")

# Prueba de hipotesis con valores Z
z_critico = -norm.ppf(alfa)

if z < z_critico:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho")