from Formulas_Estadistica.InterConf import InterConf
from Formulas_Estadistica.Comparacion import comparar_mayor_que
""" Se quiere realizar un pronóstico del precio de una acción con base en la lectura del comportamiento del precio en 
los últimos 24 días. Los datos de la fluctuación del precio diario, se muestra a continuación.
20 31 34 31 32 30 25 20 32 64 33 30 33 55 25 55 32 44 21 35 54 40 41"""

data = [20, 31, 34, 31, 32, 30,
        25, 20, 32, 64, 33, 30,
        33, 34, 55, 25, 55, 32,
        44, 21, 35, 54, 40, 41]

# A. Estime un intervalo de confianza del 95% para el precio de la acción verdadero.
InterConf.caso_dos_tres_con_datos(95, data).intervalo_rango_caso_tres()

# B. Estime un intervalo de confianza del 96% para la desviación estándar del precio de la acción.
InterConf.caso_dos_tres_con_datos(96, data).calcular_intervalo_varianza()

# C. Estime un intervalo de confianza al 85% para la proporción del valor de la acción superior a los 32 $USD/acción.
# Suponga que la distribución de los datos es normal
p_gorro = (comparar_mayor_que(data, 32)/24*100)
InterConf.intervalo_confianza_proporcion(24, p_gorro, 85).calcular_intervalo_proporcion()
