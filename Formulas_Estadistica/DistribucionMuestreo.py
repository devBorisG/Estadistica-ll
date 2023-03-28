from itertools import combinations

import pandas as pd
from numpy import var


class DistriMuestre:

    def __int__(self, datos, x_barra, var_poblacional, combinaciones):
        self.datos = datos
        self.x_barra = x_barra
        self.var_poblacional = var_poblacional
        self.combinaciones = combinaciones

    @classmethod
    def ingresar_datos(cls, datos, combinaciones):
        ingresar_datos = cls.__new__(cls)
        ingresar_datos.datos = datos
        ingresar_datos.x_barra = datos.mean(axis=1)
        ingresar_datos.var_poblacional = datos.var(axis=1, ddof=0)
        ingresar_datos.combinaciones = combinaciones
        return ingresar_datos

    def get_x_barra(self):
        return self.x_barra

    def get_var_poblacional(self):
        return self.var_poblacional

    def get_datos(self):
        return self.datos

    def get_combinaciones(self):
        return self.combinaciones

    def tabla_muestreo(self):
        dates = []
        temp = combinations(self.get_datos(), self.get_combinaciones())
        for i, j, k in temp:  # Se agregan o se quitan iteraciones (i,j,k,...) dependiendo de cuantas combinaciones
            # soliciten
            datos = f"{i} {j} {k}"
            valor_datos = (self.get_datos()[i][0], self.get_datos()[j][0], self.get_datos()[k][0])
            media_muestral = (self.get_datos()[i][0] + self.get_datos()[j][0] + self.get_datos()[k][0]) / self.get_combinaciones()
            varianza_muestral = sum((item - media_muestral) ** 2 for item in valor_datos)/(len(valor_datos)-1)
            dates.append(pd.Series([datos,
                                    valor_datos,
                                    media_muestral,
                                    varianza_muestral],
                                   index=['Datos',
                                          'Valor Datos',
                                          'Media Muestral',
                                          'Varianza Muestral']))
        df_muestreo = pd.DataFrame(dates, index=range(1, len(dates) + 1))
        return df_muestreo


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
r = DistriMuestre.ingresar_datos(data, 3)
print("Inciso a:\n\tMedia Poblacional=", r.get_x_barra(), "\n\tVarianza Poblacional=", r.get_var_poblacional())
print("Inciso b:\n", r.tabla_muestreo())
print("Inciso c:")
