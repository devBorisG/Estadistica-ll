# %% Librerías Necesarias
import pandas as pd
from math import sqrt
from statistics import mean, stdev, pstdev
from scipy.stats import norm, t, chi2


# %% Creación de la clase para estadística inferencial
class IntervalosConfianza:

    # %% Creación de todos los constructores necesarios
    def __int__(self, nivel_confianza, des_estand_poblacional, n, x_barra, des_estand_muestral, p_gorro):
        self.nivel_confianza = nivel_confianza
        self.des_estand_poblacional = des_estand_poblacional
        self.n = n
        self.x_barra = x_barra
        self.des_estand_muestral = des_estand_muestral
        self.p_gorro = p_gorro

    # Creación de instancias de clase dependiendo de los casos
    @classmethod
    def caso_uno_sin_datos(cls, nivel_confianza, des_estand_poblacional, n, x_barra):  # Población grande, o(
        # des_estand_P) conocido
        caso_uno_sin_datos = cls.__new__(cls)
        caso_uno_sin_datos.nivel_confianza = nivel_confianza
        caso_uno_sin_datos.des_estand_poblacional = des_estand_poblacional
        caso_uno_sin_datos.n = n
        caso_uno_sin_datos.x_barra = x_barra
        return caso_uno_sin_datos  # ESTE CASO SE USA CUANDO NO NOS DAN LOS DATOS SINO SIMPLEMENTE LA CANTIDAD DE LA
        # MUESTRA

    @classmethod
    def caso_uno_con_datos(cls, nivel_confianza, datos):  # Población grande, o(des_estand_P) conocida
        caso_uno_con_datos = cls.__new__(cls)
        caso_uno_con_datos.nivel_confianza = nivel_confianza
        caso_uno_con_datos.des_estand_poblacional = pstdev(datos)
        caso_uno_con_datos.n = len(datos)
        caso_uno_con_datos.x_barra = mean(datos)
        return caso_uno_con_datos  # ESTE CASO SE USA CUANDO NOS DAN UNA CANTIDAD DE DATOS MAYOR A 30 Y NOS DAN UNA
        # BASE DE DATOS O INFORMACIÓN

    @classmethod
    def caso_dos_tres_con_datos(cls, nivel_confianza, datos):  # Población grande, o(des_estand_P) desconocida
        caso_dos_tres_con_datos = cls.__new__(cls)
        caso_dos_tres_con_datos.nivel_confianza = nivel_confianza
        caso_dos_tres_con_datos.n = len(datos)
        caso_dos_tres_con_datos.x_barra = mean(datos)
        caso_dos_tres_con_datos.des_estand_muestral = stdev(datos)
        return caso_dos_tres_con_datos  # ESTE CASO SE USA CUANDO NOS DAN UNA CANTIDAD DE DATOS MAYOR A 30 Y NOS DAN UNA
        # BASE DE DATOS O INFORMACIÓN

    @classmethod
    def caso_dos_tres_sin_datos(cls, nivel_confianza, n, x_barra, des_estand_muestral):  # Población grande, o(
        # des_estand_P) desconocida
        caso_dos_tres_sin_datos = cls.__new__(cls)
        caso_dos_tres_sin_datos.nivel_confianza = nivel_confianza
        caso_dos_tres_sin_datos.n = n
        caso_dos_tres_sin_datos.x_barra = x_barra
        caso_dos_tres_sin_datos.des_estand_muestral = des_estand_muestral
        return caso_dos_tres_sin_datos  # ESTE CASO SE USA CUANDO NOS DAN UNA CANTIDAD DE DATOS MAYOR A 30 Y NOS DAN
        # SIMPLEMENTE EL VALOR DE LA MUESTRA

    @classmethod
    def intervalo_confianza_proporcion(cls, n, p_gorro, nivel_confianza):
        intervalo_confianza_proporcion = cls.__new__(cls)
        intervalo_confianza_proporcion.n = n
        intervalo_confianza_proporcion.p_gorro = p_gorro
        intervalo_confianza_proporcion.nivel_confianza = nivel_confianza
        return intervalo_confianza_proporcion

    @classmethod
    def intervalo_confianza_varianza_con_datos(cls, datos, nivel_confianza):
        intervalo_confianza_varianza_con_datos = cls.__new__(cls)
        intervalo_confianza_varianza_con_datos.n = len(datos)
        intervalo_confianza_varianza_con_datos.des_estand_muestral = stdev(datos)
        intervalo_confianza_varianza_con_datos.nivel_confianza = nivel_confianza
        return intervalo_confianza_varianza_con_datos

    @classmethod
    def intervalo_confianza_varianza_sin_datos(cls, n, des_estand_muestral,nivel_confianza):
        intervalo_confianza_varianza_con_datos = cls.__new__(cls)
        intervalo_confianza_varianza_con_datos.n = n
        intervalo_confianza_varianza_con_datos.des_estand_muestral = des_estand_muestral
        intervalo_confianza_varianza_con_datos.nivel_confianza = nivel_confianza
        return intervalo_confianza_varianza_con_datos

    # %% Creación de getters
    def get_nivel_confianza(self):
        return self.nivel_confianza

    def get_des_estand_poblacional(self):
        return self.des_estand_poblacional

    def get_n(self):
        return self.n

    def get_x_barra(self):
        return self.x_barra

    def get_des_estand_muestral(self):
        return self.des_estand_muestral

    def get_p_gorro(self):
        return self.p_gorro

    # %% Creación de Métodos
    def intervalo_rango_caso_uno(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        z = norm.ppf(alpha_medios)
        limite_inferior = self.get_x_barra() + (z * self.get_des_estand_poblacional() / sqrt(self.get_n()))
        limite_superior = self.get_x_barra() - (z * self.get_des_estand_poblacional() / sqrt(self.get_n()))
        intervalos_confianza = [limite_inferior, limite_superior]
        w = limite_superior - limite_inferior
        print("El intervalo de confianza es:", intervalos_confianza)
        print("El rango es:", w)

    def intervalo_rango_caso_dos(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        z = norm.ppf(alpha_medios)
        limite_inferior = self.get_x_barra() + (z * self.get_des_estand_muestral() / sqrt(self.get_n()))
        limite_superior = self.get_x_barra() - (z * self.get_des_estand_muestral() / sqrt(self.get_n()))
        intervalos_confianza = [limite_inferior, limite_superior]
        w = limite_superior - limite_inferior
        print("El intervalo de confianza es:", intervalos_confianza)
        print("El rango es:", w)

    def intervalo_rango_caso_tres(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        t_student = t.ppf(alpha_medios, self.get_n() - 1)
        limite_inferior = self.get_x_barra() + (t_student * self.get_des_estand_muestral() / sqrt(self.get_n()))
        limite_superior = self.get_x_barra() - (t_student * self.get_des_estand_muestral() / sqrt(self.get_n()))
        intervalos_confianza = [limite_inferior, limite_superior]
        w = limite_superior - limite_inferior
        print("El intervalo de confianza es:", intervalos_confianza)
        print("El rango es:", w)

    def calcular_intervalo_proporcion(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        z = norm.ppf(alpha_medios)
        p_gorro_decimal = self.get_p_gorro()/100
        lim_inferior = (p_gorro_decimal + (z**2/2*self.get_n()) + (z * sqrt((p_gorro_decimal*(1-p_gorro_decimal)/self.get_n())+(z**2/4*self.get_n()**2))))/(1+(z**2/self.get_n()))
        lim_superior = (p_gorro_decimal + (z**2/2*self.get_n()) - (z * sqrt((p_gorro_decimal*(1-p_gorro_decimal)/self.get_n())+(z**2/4*self.get_n()**2))))/(1+(z**2/self.get_n()))
        intervalo_confianza = [lim_inferior, lim_superior]
        w = lim_superior - lim_inferior
        print("El intervalo de confianza tiene el estimado de:", intervalo_confianza)
        print("El rango es:", w)

    def calcular_intervalo_varianza(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        uno_menos_alpha_medios = alpha/2
        alpha_medios = (self.get_nivel_confianza()/100) + uno_menos_alpha_medios
        s_cuadrado = self.get_des_estand_muestral()**2
        chi_cuadrado_inf = chi2.ppf(alpha_medios, self.get_n()-1)
        chi_cuadrado_sup = chi2.ppf(uno_menos_alpha_medios, self.get_n()-1)
        lim_inferior = ((self.get_n()-1)*s_cuadrado)/chi_cuadrado_inf
        lim_superior = ((self.get_n()-1)*s_cuadrado)/chi_cuadrado_sup
        intervalos_confianza = [lim_inferior, lim_superior]
        w = lim_superior - lim_inferior
        print("El intervalo de confianza tiene el estimado de:", intervalos_confianza)
        print("El rango es:", w)

# %% Inicio de Pruebas
# Prueba para caso uno sin datos de muestra
nivel = 95
des_poblacional = 5
muestra = 40
media = 68
respuesta = IntervalosConfianza.caso_uno_sin_datos(nivel, des_poblacional, muestra, media)
respuesta.intervalo_rango_caso_uno()

# Prueba para caso dos con datos de muestra
data_base = pd.read_excel("C:/Users/david/Documents/IntervalosDeConfianza.xlsx", sheet_name="Media Caso ll")
data_base = data_base["Datos TRM"]
print("Datos Ejercicio 2: \n", data_base)
respuesta = IntervalosConfianza.caso_dos_tres_con_datos(92, data_base)
respuesta.intervalo_rango_caso_dos()

# Prueba para caso tres con datos de muestra
dates = [16, 17, 10, 19, 21, 14, 22, 19, 8]
print("Datos ejercicio 3: \n", dates)
respuesta = IntervalosConfianza.caso_dos_tres_con_datos(90, dates)
respuesta.intervalo_rango_caso_tres()

# Prueba para los intervalos de confianza con la proporción
"""En una empresa de manufactura, se realizó un estudio de calidad para encontrar los
artículos que pasan las pruebas de certificación, se encontró que en una muestra de 100
productos el 85 pasan la prueba Estime un intervalo de confianza del 97 5 para la
cantidad de artículos que verdaderamente pasan las pruebas de certificación"""

print("Ejercicio 4: \n")
IntervalosConfianza.intervalo_confianza_proporcion(6900, 85, 97.5).calcular_intervalo_proporcion()

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
IntervalosConfianza.intervalo_confianza_varianza_con_datos([1470, 2200, 1510, 2290, 1690, 2380, 1740, 2390, 1900, 2480,
                                                            2000, 2500, 2030, 2580, 2100, 2700, 2190], 95)\
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
IntervalosConfianza.caso_dos_tres_con_datos(90, prescripciones).intervalo_rango_caso_tres()

print("Inciso b:")
print(" b1:")
IntervalosConfianza.caso_dos_tres_con_datos(95, prescripciones).intervalo_rango_caso_tres()
print(" b2:")
IntervalosConfianza.caso_dos_tres_con_datos(98, prescripciones).intervalo_rango_caso_tres()
