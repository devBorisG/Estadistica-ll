from scipy.stats import norm, t, chi2
from Formulas_Estadistica.InterConf import InterConf
from Formulas_Estadistica.TamaMuest import TamaMuest
"""En una empresa de manufactura, se sabe que el gasto energético por unidad fabricada está normalmente distribuido con
un intervalo de confianza al 95% de (0.1 a 0.18) kWh. Esta estimación se contabilizó durante la fabricación de 150
piezas."""

#  A. Si para el mes siguiente se quieren fabricar un total de 15,000 unidades. Estime un intervalo de confianza al 98%
# de la energía necesaria para cumplir con la meta.
InterConf.caso_dos_tres_sin_datos(98, 15000, 130, 240).intervalo_rango_caso_dos()

# B. Si se quiere lograr un intervalo de confianza con un ancho de 0.1 kWh/unidad a un nivel de confianza del 99%,
# ¿qué tamaño de muestra se debió seleccionar para realizar el estudio? Suponga que los datos se distribuyen normal y
# la desviación estándar es 30 kWh.
TamaMuest.tamano_media(30, 99, 0.1).calcular_tamano_muestra_media()

# C. Estime para el intervalo de confianza del numeral A, un intervalo de confianza del 99% para la desviación estándar
# del consumo energético por unidad fabricada.

print(norm.ppf((1-0.99)/2))
