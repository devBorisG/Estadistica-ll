from math import sqrt

import sympy as sp
import pandas as pd
from scipy.stats import norm

import Formulas_Estadistica.DistribucionMuestreo as dm
import Formulas_Estadistica.Comparacion as cp
import Formulas_Estadistica.Teoremas as teo
import Formulas_Estadistica.DatosIntegral as dt
import Formulas_Estadistica.InterConf as ic
#%% Sección pregunta 1
""""""
"""Pregunta 1
En el mercado de cierta ciudad, 5 tiendas ofertan el mismo producto, pero a diferentes precios, tal como se muestra en
la tabla (unidades $COP).
"""

pregunta1 = pd.DataFrame({'P1': [35000],
                          'P2': [25000],
                          'P3': [35500],
                          'P4': [26000],
                          'P5': [25000]})

"""Si se realiza un muestreo con n=3, responda:
A.     ¿Cuántas muestras es posible seleccionar de la población?
B.     ¿Cuál es el valor de la media y la desviación estándar poblacional?
C.     ¿Cuál es la probabilidad de obtener una media muestral igual a 28,500 $COP?
D.     ¿Cuál es la probabilidad de seleccionar una media muestral superior a la media poblacional?
E.     ¿Cuál es la probabilidad de seleccionar una media muestral inferior a 30,000 $COP?
F.      ¿Cuál es la probabilidad de seleccionar una media muestral entre 28,000 y 30,000 $COP?
G.    ¿Cuál es la probabilidad de obtener una varianza muestral igual a 28,583,333.3 $COP2?
H.    ¿Cuál es la probabilidad de obtener una varianza muestral superior a 33,333,333.3 $COP2?
I.       ¿Cuál es la probabilidad de obtener una varianza muestral entre 28,583,333.3 y 33,583,333.3 $COP2?
"""

respuesta1 = dm.DistriMuestre.creacion_tablas_combinacion(pregunta1, 3)
tabla_muestreo = respuesta1.tabla_muestreo_combinatoria()

"Respuesta Pregunta 1 Inciso A"

p1a = len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso B"

p1b1 = respuesta1.get_x_barra()

p1b2 = sqrt(respuesta1.get_var_poblacional())

"Respuesta Pregunta 1 Inciso C"

p1c = cp.comparar_iguales(respuesta1.tabla_muestreo_combinatoria().Media_Muestral, 28500)/len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso D"

p1d = cp.comparar_mayor_que(respuesta1.tabla_muestreo_combinatoria().Media_Muestral, respuesta1.get_x_barra())/len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso E"

p1e = cp.comparar_menor_que(respuesta1.tabla_muestreo_combinatoria().Media_Muestral, 30000)/len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso F"

p1f = cp.comparar_entre_sin_incluir(respuesta1.tabla_muestreo_combinatoria().Media_Muestral, 28000, 30000)/len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso G"

p1g = cp.comparar_iguales(respuesta1.tabla_muestreo_combinatoria().Varianza_Muestral, 28583333.3)/len(respuesta1.tabla_muestreo_combinatoria())
# Aquí existe una pequeña variación, ya que en la tabla de muestreo creada la varianza muestral esta calculada con 7
# decimales entonces para solucionar el problema se propone que según cuantos decimales se tomen en el parcial
# ir directamente a la función "tabla_muestreo_combinatoria" y aplicar un round(###,1) para ajustar la cantidad
# de decimales que se desean mostrar

"Respuesta Pregunta 1 Inciso H"

p1h = cp.comparar_mayor_que(respuesta1.tabla_muestreo_combinatoria().Varianza_Muestral, 33333333.3)/len(respuesta1.tabla_muestreo_combinatoria())

"Respuesta Pregunta 1 Inciso I"

p1i = cp.comparar_entre_sin_incluir(respuesta1.tabla_muestreo_combinatoria().Varianza_Muestral, 28583333.3, 33583333.3)/len(respuesta1.tabla_muestreo_combinatoria())

#%% Sección pregunta 3
"""Pregunta 3
La cantidad de carga (en toneladas) que puede transportar los vehículos de una compañía de 
construcción, se distribuye de acuerdo con la ecuación mostrada a continuación: 

"""
x = sp.Symbol('x')
fx = (3/2)*(1-x**2)  # Función

"""De acuerdo con la información suministrada, responda las siguientes preguntas:
A.     ¿Cuál es la media poblacional de la capacidad de carga que pueden transportar los vehículos de la compañía?
B.     ¿Cuál es la varianza poblacional de la capacidad de carga que pueden transportar los vehículos de la compañía?
C.     ¿Cuál es la desviación estándar poblacional de la capacidad de carga que pueden transportar los vehículos de la compañía?
D.     Si se selecciona una muestra de 50 vehículos de carga, ¿Cuál es la probabilidad de que la media muestral sea superior a media tonelada?
E.     Si se selecciona una muestra de 20 vehículos, ¿Cuál es el valor de la media que está por encima del 20% de las muestras?
F.      Si se selecciona una muestra de 50 vehículos, ¿Cuál es la probabilidad de que la varianza muestral sea mayor que la poblacional? (utiliza la función =DISTR.CHICUAD() en Excel).
"""

respuesta3 = dt.DatosIntegral.calculo_integral(fx, 0, 1)

"Respuesta Pregunta 3 Inciso A"

p3a = respuesta3.get_media_poblacional()

"Respuesta Pregunta 3 Inciso B"

p3b = respuesta3.get_var_poblacional()

"Respuesta Pregunta 3 Inciso C"

p3c = respuesta3.get_des_estand_poblacional()

"Respuesta Pregunta 3 Inciso D"

p3d = 1-teo.probabilidad_z(teo.teorema_limite_central(0.5, p3a, p3c, 50))

#%% Sección pregunta 4
"""Pregunta 4 
En una fabrica de encuadernación el 89.98 % de los libros pasan la prueba de calidad. Si se selecciona 
una muestra de 40 libros. Responda:
A.     ¿Cuál es la probabilidad de que menos del 20% de los libros no pasen la prueba?
B.     ¿Cuál es la probabilidad de que la proporción muestral sea superior a la proporción poblacional?
C.     ¿Cuál es la probabilidad de que más del 95 % de los libros pasen la prueba?
D.     ¿Qué valor de proporción está por debajo del 25 % de todas las posibles muestras que se puedan seleccionar?
"""

"Respuesta Pregunta 4 Inciso A"

p4a = teo.probabilidad_z(teo.teorema_proporcion(80, 89.98, 40))

"Respuesta Pregunta 4 Inciso B"



"Respuesta Pregunta 4 Inciso C"

p4c = teo.probabilidad_z(teo.teorema_proporcion(95, 89.98, 40))

"Respuesta Pregunta 4 Inciso D"



#%% Sección pregunta 5

"""Pregunta 5
Encuentre el valor de la probabilidad “P” o de “Z” según sea el caso
"""

"Respuesta Pregunta 5 Inciso A"

p5a = teo.probabilidad_z(-1.50)

"Respuesta Pregunta 5 Inciso B"

p5b = 1-teo.probabilidad_z(-2.56)

"Respuesta Pregunta 5 Inciso C"

p5e = norm.ppf(0.35)

"Respuesta Pregunta 5 Inciso D"

p5d = norm.ppf(0.65)*-1

"Respuesta Pregunta 5 Inciso E"

p5e = teo.probabilidad_z(1.36) - teo.probabilidad_z(-1.02)

"Respuesta Pregunta 5 Inciso F"



#%% Sección pregunta 6
"""Pregunta 6
En una determinada empresa, se seleccionó al azar una muestra de 350 empleados cuya media de ingresos mensuales resultó 
igual a $ 4,550,000 COP, con una desviación de $ 830,000 COP.

A.     Halle un intervalo de confianza al 97.5 % para la media de los ingresos mensuales de todos los empleados de la 
empresa. 
B.     Halle un intervalo de confianza al 92% para la media de los ingresos mensuales de todos los empleados 
de la empresa.
"""

"Respuesta Pregunta 6 Inciso A"

ic.InterConf.caso_uno_sin_datos(97.5, 830000, 350, 4550000).intervalo_rango_caso_uno()

"Respuesta Pregunta 6 Inciso B"

ic.InterConf.caso_uno_sin_datos(92, 830000, 350, 4550000).intervalo_rango_caso_uno()
