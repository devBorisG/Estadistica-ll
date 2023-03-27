# %% Librerías Necesarias
import pandas as pd
from math import sqrt
from statistics import mean, stdev, pstdev
from scipy.stats import norm, t


# %% Creación de la clase para estadística inferencial
class EstadisticaInferencial:

    # %% Creación de todos los constructores necesarios
    def __int__(self, nivel_confianza, des_estand_poblacional, n, x_barra, des_estand_muestral):
        self.nivel_confianza = nivel_confianza
        self.des_estand_poblacional = des_estand_poblacional
        self.n = n
        self.x_barra = x_barra
        self.des_estand_muestral = des_estand_muestral

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


# %% Inicio de Pruebas
# Prueba para caso uno sin datos de muestra
nivel = 95
des_poblacional = 5
muestra = 40
media = 68
respuesta = EstadisticaInferencial.caso_uno_sin_datos(nivel, des_poblacional, muestra, media)
respuesta.intervalo_rango_caso_uno()

# Prueba para caso dos con datos de muestra
data_base = pd.read_excel("C:/Users/david/Documents/IntervalosDeConfianza.xlsx", sheet_name="Media Caso ll")
data_base = data_base["Datos TRM"]
print("Datos Ejercicio 2: \n", data_base)
respuesta = EstadisticaInferencial.caso_dos_tres_con_datos(92, data_base)
respuesta.intervalo_rango_caso_dos()

# Prueba para caso tres con datos de muestra
dates = [16, 17, 10, 19, 21, 14, 22, 19, 8]
print("Datos ejercicio 3: \n", dates)
respuesta = EstadisticaInferencial.caso_dos_tres_con_datos(90, dates)
respuesta.intervalo_rango_caso_tres()
