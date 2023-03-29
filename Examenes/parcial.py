import pandas as pd
from Formulas_Estadistica.DistribucionMuestreo import DistriMuestre
from Formulas_Estadistica.Comparacion import comparar_mayor_que, comparar_menor_que

print("Ejercicio Distribución de Muestreo 1")
data = pd.DataFrame({'E1': [6],
                     'E2': [4],
                     'E3': [3],
                     'E4': [6],
                     'E5': [2]})

print(data)
r = DistriMuestre.creacion_tablas_combinacion(data, 3)
print("Inciso a:\n\tMedia Poblacional=", r.get_x_barra(), "\n\tVarianza Poblacional=", r.get_var_poblacional())
print("Inciso b:\n", r.get_tabla_muestreo())
print("Inciso c:\n\tDistribución Muestreo media\n", r.get_dis_tabla_prob(), "\n\tVarianza\n", r.get_prob_var())
print("Inciso d:", comparar_mayor_que(r.get_tabla_muestreo().Media_Muestral, 4)/len(r.get_tabla_muestreo()))
print("Inciso e:", comparar_menor_que(r.get_tabla_muestreo().Varianza_Muestral, 2)/len(r.get_tabla_muestreo()))
