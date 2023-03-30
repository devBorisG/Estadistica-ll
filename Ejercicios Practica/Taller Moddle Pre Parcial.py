from math import sqrt

import pandas as pd
import Formulas_Estadistica.DistribucionMuestreo as dt
import Formulas_Estadistica.Comparacion as cp
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

respuesta1 = dt.DistriMuestre.creacion_tablas_combinacion(pregunta1, 3)
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

"""Pregunta 3
La cantidad de carga (en toneladas) que puede transportar los vehículos de una compañía de 
construcción, se distribuye de acuerdo con la ecuación mostrada a continuación: 

"""

"""Pregunta 4 En una fabrica de encuadernación el 89.98 % de los libros pasan la prueba de calidad. Si se selecciona 
una muestra de 40 libros. Responda:
A.     ¿Cuál es la probabilidad de que menos del 20% de los libros no pasen la prueba?
B.     ¿Cuál es la probabilidad de que la proporción muestral sea superior a la proporción poblacional?
C.     ¿Cuál es la probabilidad de que más del 95 % de los libros pasen la prueba?
D.     ¿Qué valor de proporción está por debajo del 25 % de todas las posibles muestras que se puedan seleccionar?
"""