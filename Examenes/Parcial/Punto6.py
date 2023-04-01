from math import sqrt

import sympy as sp
import Formulas_Estadistica.DatosIntegral as dt
import Formulas_Estadistica.Teoremas as teo

x = sp.Symbol('x')

fx = (4/3)*((x**2-1)**2)

r = dt.DatosIntegral.calculo_integral(fx, 0, 1.4876)

"Punto a"

miu = r.get_media_poblacional()

sigma = r.get_des_estand_poblacional()

sigma2 = r.get_var_poblacional()

"Punto b"

pb = teo.probabilidad_z(teo.teorema_limite_central(miu, miu, sqrt(sigma2), 100))

"Punto c"

pc = 1 - teo.probabilidad_z(teo.teorema_limite_central(0.5, miu, sqrt(sigma2), 100))

"Punto d"

pd = teo.probabilidad_chi2(teo.teorema_varianza(50, 0.7, sigma2), 50) - teo.probabilidad_chi2(teo.teorema_varianza(50, 0.3, sigma2), 50)

