from scipy.stats import f
#%% Punto A
"""A: ¿Cuál es la variación a causa de los tratamientos?,

580.3019 m2
1.2274 m2
145.0755 m2
21.0685 m2

"""
ss_tra = 580.3019  # Suma cuadrado de tratamiento
k = 5  # Número de tratamientos
gl_tra = k - 1  # Grados de libertad para los tratamientos
cm_tra = ss_tra/gl_tra  # Se calcula la variación/varianza para los tratamientos
print("Variación a causa de los tratamientos es:", cm_tra, "m2")  # RESPUESTA: 145.0755 m2

#%% Punto B
"""B: ¿Cuál es la variación total de la variable respuesta del experimento?,

610.9871 m2
145.3019 m2
21.0685 m2
1.2274 m2

"""

# Primero se debe calcular también la variación del error
sse = 30.6852  # Suma cuadrado de error
N = 30  # Número total de observaciones: 5 tratamientos cada uno con 6 observaciones
gl_e = N - k  # Grados de libertad para el error
cme = sse/gl_e  # Se calcula la variación/varianza para el error
# Ahora sigue calcular la varianza total
# Para calcular la total se despeja la fórmula original quedando: SST = SSE + SS_TRA
sst = sse + ss_tra  # Suma cuadrado total
gl_t = N - 1  # Grados de libertad para total
cmt = sst/gl_t
print("Variación total de la variable respuesta es:", cmt, "m2")  # RESPUESTA: 1.2274 m2

#%% Punto C
"""C: De acuerdo con el valor P estimado y un nivel de significancia del 1%, ¿Es correcto afirmar que los rotores seleccionados influyen estadísticamente sobre la cabeza máxima de la bomba centrifuga?

Verdadero
Falso

"""
# Hallamos F
Fcalc = cm_tra/cme  # Estadístico de prueba para evaluar la hypothesis de interés
# Valor P para prueba de hipótesis
P = 1 - f.cdf(Fcalc, gl_tra, gl_e)  # Para valores P
print("El valor P para la Fcalc es:", P)
if P < 0.01:
    print("Se rechaza Ho")
else:
    print("No se rechaza Ho")
