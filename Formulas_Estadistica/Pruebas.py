from InterConf import InterConf
from TamaMuest import TamaMuest
from DistribucionMuestreo import DistriMuestre
import pandas as pd
# %% Inicio de Pruebas Intervalos confianza
# Prueba para caso uno sin datos de muestra
nivel = 95
des_poblacional = 5
muestra = 40
media = 68
respuesta = InterConf.caso_uno_sin_datos(nivel, des_poblacional, muestra, media)
respuesta.intervalo_rango_caso_uno()

# Prueba para caso dos con datos de muestra
data_base = pd.read_excel("C:/Users/david/Documents/IntervalosDeConfianza.xlsx", sheet_name="Media Caso ll")
data_base = data_base["Datos TRM"]
print("Datos Ejercicio 2: \n", data_base)
respuesta = InterConf.caso_dos_tres_con_datos(92, data_base)
respuesta.intervalo_rango_caso_dos()

# Prueba para caso tres con datos de muestra
dates = [16, 17, 10, 19, 21, 14, 22, 19, 8]
print("Datos ejercicio 3: \n", dates)
respuesta = InterConf.caso_dos_tres_con_datos(90, dates)
respuesta.intervalo_rango_caso_tres()

# Prueba para los intervalos de confianza con la proporción
"""En una empresa de manufactura, se realizó un estudio de calidad para encontrar los
artículos que pasan las pruebas de certificación, se encontró que en una muestra de 100
productos el 85 pasan la prueba Estime un intervalo de confianza del 97 5 para la
cantidad de artículos que verdaderamente pasan las pruebas de certificación"""

print("Ejercicio 4: \n")
InterConf.intervalo_confianza_proporcion(6900, 85, 97.5).calcular_intervalo_proporcion()

"""Los datos adjuntos del precio de arrendamiento en un sector de Miami en USD, se
muestran a continuación:
1470
1510
1690
1740
1900
2000
2030
2100
2190
2200
2290
2380
2390
2480
2500
2580
2700
Estime un intervalo de confianza del 95 para σ 2
"""

print("Ejercicio 5")
InterConf.intervalo_confianza_varianza_con_datos([1470, 2200, 1510, 2290, 1690, 2380, 1740, 2390, 1900, 2480,
                                                  2000, 2500, 2030, 2580, 2100, 2700, 2190], 95) \
    .calcular_intervalo_varianza()

"""Existen varios medicamentos para tratar la diabetes Un experto en ventas de una importante compañía
farmacéutica necesita una estimación del número de nuevas prescripciones de su nuevo medicamento
contra la diabetes que se hicieron durante un determinado mes El número de nuevas prescripciones en una
muestra de 10 distritos de ventas es
210
240
190
275
290
265
310
284
2631
243

a) Halle el intervalo de confianza al 90 del número medio de prescripciones de este nuevo medicamento
en todos los distritos de ventas
b) Calcule la amplitud de los intervalos de confianza al 95 y 98
c) Encuentro un intervalo de confianza del 90 para la varianza
"""

print("Ejercicio aplicado 1: ")
print("Inciso a:")
prescripciones = [210, 265, 240, 310, 190, 284, 275, 263, 290, 243]
InterConf.caso_dos_tres_con_datos(90, prescripciones).intervalo_rango_caso_tres()

print("Inciso b:")
print(" b1:")
InterConf.caso_dos_tres_con_datos(95, prescripciones).intervalo_rango_caso_tres()
print(" b2:")
InterConf.caso_dos_tres_con_datos(98, prescripciones).intervalo_rango_caso_tres()
print("Inciso c:")
InterConf.intervalo_confianza_varianza_con_datos(prescripciones, 90).calcular_intervalo_varianza()


#%% Inicio de pruebas Tamaño de la muestra
# Ejercicio para tamaño de la muestra con la media
"""Un intensivo monitoreo a un sistema operativo sugiere que el tiempo de respuesta a un comando
de edición particular está normalmente distribuido con σ = 25 ms.

Se instaló un nuevo sistema operativo y se desea estimar el tiempo de respuesta promedio
verdadero µ en el nuevo entorno . Suponiendo que los tiempo de respuesta siguen estando
normalmente distribuidos con σ = 25 ms.
¿Que tamaño de muestra es necesario para asegurarse de que el intervalo de confianza del 95 %
resultante tiene un ancho de cuando mucho 10 ms
"""

TamaMuest.tamano_media(25, 95, 10).calcular_tamano_muestra_media()

# Ejercicio para tamaño de la muestra con la proporción
"""Del ejemplo anterior estime el tamaño de muestra para que el intervalo de confianza del
98 tenga un ancho de 2"""

TamaMuest.tamano_proporcion(85, 0.02, 98).calcular_tamano_muestra_proporcion()

#%% Inicio de pruebas tablas distribución de muestreo
"""En un salón hay 5 estudiantes, cada uno se encuentra cursando un semestre diferente como
se muestra en los datos presentados a continuación
E1 6
E2 4
E3 3
E4 6
E5 2

De acuerdo con la información presentada responda las siguientes preguntas
a) ¿Cuál es la media poblacional y la varianza poblacional de los semestres cursados?
b) Si se selecciona una muestra n= 3 estudiantes, ¿De cuantas posibles formas puedo
seleccionar la muestra?
c) Estime la distribución de muestreo para la media y para la varianza
d) ¿Cuál es la probabilidad de seleccionar una media muestral mayor a 4
e) ¿Cuál es la probabilidad de seleccionar una varianza muestral menor a 2
"""

print("Ejercicio Distribución de Muestreo 1")
data = pd.DataFrame({'E1': [6],
                     'E2': [4],
                     'E3': [3],
                     'E4': [6],
                     'E5': [2]})
print(data)
r = DistriMuestre.creacion_tablas(data, 3)
print("Inciso a:\n\tMedia Poblacional=", r.get_x_barra(), "\n\tVarianza Poblacional=", r.get_var_poblacional())
print("Inciso b:\n", r.get_tabla_muestreo())
print("Inciso c:\n\tDistribución Muestreo media", r.get_dis_tabla_prob(), "\n\tVarianza", r.get_prob_var())
