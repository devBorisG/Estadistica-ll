from Formulas_Estadistica.InterConf import InterConf
"""Existen varios medicamentos para tratar la diabetes. Un experto en ventas de una importante compañía farmacéutica
necesita una estimación del número de nuevas prescripciones de su nuevo medicamento contra la diabetes que se hicieron
durante un determinado mes. El número de nuevas prescripciones en una muestra de 10 distritos de ventas es
210 340 190 275 390 265 210 284 263 243"""

data = [210, 340, 190, 275, 390, 265, 210, 284, 263, 243]

# A. Halle el intervalo de confianza al 95 % del número medio de prescripciones de este nuevo medicamento en todos los
# distritos de ventas.
InterConf.caso_dos_tres_con_datos(95, data).intervalo_rango_caso_tres()

# B. Calcule la amplitud de un intervalo de confianza al 98%
InterConf.caso_dos_tres_con_datos(98, data).intervalo_rango_caso_tres()

# C. Encuentre un intervalo de confianza del 95 % para la desviación estándar de las ventas del medicamento
InterConf.caso_dos_tres_con_datos(95, data).calcular_intervalo_varianza()