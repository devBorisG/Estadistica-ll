import numpy as np
from itertools import combinations
from scipy.stats import t,f
import matplotlib.pyplot as plt

import pandas as pd


class Unifactorial:
    def __init__(self, dataframe: pd.DataFrame):  # Se ingresa el excel
        """
    The __init__ function is the constructor of the class. It initializes all the attributes that are needed for
    the rest of the functions to work properly. The dataframe attribute is initialized with whatever dataframe was passed
    to it when creating an instance of this class.

    :param self: Represent the instance of the class
    :param dataframe: Store the dataframe that will be used in the class
    :return:  object (self) that we’ll use to access the rest of the methods
    :doc-author: David
    """
        self.dataframe = dataframe
        self.yij2 = np.square(dataframe)  # Se elevan todas las observaciones al cuadrado
        self.yij2["total"] = self.yij2.sum(axis=1)  # sumamos los cuadrados de cada tratamiento
        self.sumayij2 = sum(self.yij2["total"])  # Estimamos la suma cuadrada de todas las observaciones de la matriz
        # de datos
        self.k = len(self.dataframe.index)  # Calculamos el número de tratamientos contando el número de filas en la
        # matriz de datos
        self.n = len(self.dataframe.columns)  # Contamos el número de observaciones por tratamiento contando las
        # columnas de la matriz de datos
        self.N = self.k * self.n  # encontramos el número total de observaciones
        self.dataframe["medias"] = self.dataframe.mean(axis=1)  # encontramos las medias de cada tratamiento y la
        # añadimos a la matriz de datos
        self.dataframe["Total"] = self.__suma_totales()  # Calculamos y añadimos la columna de totales a nuestra matriz
        # de datos
        self.totales = self.dataframe["Total"].tolist()  # Convertimos la columna de totales en una lista
        self.y_total = sum(self.dataframe["Total"])  # Calculamos "y.." sumando los elementos de la columna de totales
        self.suma_cuadrados_yi = self.__suma_cuadrados()  # Aquí calculamos la suma cuadrados de los "yi.^2"
        self.ss_tra = (1/self.n)*self.suma_cuadrados_yi-((self.y_total**2)/self.N)  # Se calcula la suma de cuadrados
        # para los tratamientos
        self.sst = self.sumayij2-((self.y_total**2)/self.N)  # Se calcula suma de cuadrados total
        self.sse = self.sst - self.ss_tra  # Se calcula suma de cuadrados de los tratamientos
        self.gl_tra = self.k - 1
        self.gl_t = self.N - 1
        self.gl_e = self.N - self.k
        self.cm_tra = self.ss_tra / self.gl_tra  # Varianza para los tratamientos
        self.cmt = self.sst / self.gl_t  # Varianza total
        self.cme = self.sse / self.gl_e  # Varianza para el error

    def __suma_totales(self):
        """
    The __suma_totales function is a private function that sums the values of all the columns in a dataframe.
    It takes no arguments and returns an integer value.

    :param self: Allow an object to refer to itself inside a class
    :return: The sum of the values in each row
    :doc-author: David
    """
        total = 0
        for i in range(1, self.n + 1):
            total += self.dataframe[i]
        return total

    def __suma_cuadrados(self):
        """
    The __suma_cuadrados function is a helper function that calculates the sum of squares for the chi-squared test.
    It takes no arguments and returns an integer value.

    :param self: Access the attributes of the class
    :return: The sum of the squared values of the array totales
    :doc-author: David
    """
        total = 0
        for i in range(self.k):
            total += self.totales[i]**2
        return total

    def comprobacion_hipotesis(self, nivel_significancia: float):
        """
        The comprobacion_hipotesis function takes a nivel_significancia as an argument and returns the result of the
        hypothesis test.

    :param self: Represent the instance of the class
    :param nivel_significancia: float: Set the significance level for the test
    :return: A boolean value
    :doc-author: David
    """
        # Para F Calculada
        f_calc = self.cm_tra / self.cme

        # Para valores P
        p = 1 - f.cdf(f_calc, self.gl_tra, self.gl_e)
        print("El valor P para Fcalc es:", p)
        if p < nivel_significancia:
            print("Se rechaza Ho")  # Existen anomalies en las observaciones que pueden afectan el experimento
        else:
            print("No se rechaza Ho")  # No existen anomalies que afecten directamente a la variable de experimento

    def metodo_lsd_dca(self):
        """
    The metodo_lsd_dca function takes the dataframe and calculates the LSD method for DCA.
        It returns a table with the pairs of means, their difference and if they are significant or not.

    :param self: Represent the instance of the class
    :return: A table with the results of the lsd method
    :doc-author: David
    """
        medias = self.dataframe["medias"].tolist()  # Volvemos la columna de medias de la tabla de datos una lista
        comb = combinations(medias, 2)
        tabla_lsd = pd.DataFrame()  # Aquí consignamos los resultados del método LSD
        parejas = []
        diferencia = []
        conclusion = []
        t_alfa = -t.ppf(0.025, self.N-self.k)
        lsd = t_alfa*np.sqrt(self.cme*((1/self.n)+(1/self.n)))
        for row in list(comb):
            parejas.append(row)
            diferencia.append(abs(row[0]-row[1]))
            if abs(row[0]-row[1]) >= lsd:
                conclusion.append("Significativa")
            else:
                conclusion.append("No significativa")
        tabla_lsd["Parejas"] = parejas
        tabla_lsd["Diferencia"] = diferencia
        tabla_lsd["Conclusión"] = conclusion

        # Gráficos de medias
        intervalo_c = t_alfa*np.sqrt(self.cme/(self.N/2))
        for i in range(self.k):
            media = medias[i]
            i_sup = media + intervalo_c
            i_inf = media - intervalo_c
            plt.plot([i, i, i], [i_inf, media, i_sup], linewidth=2, marker=".", color="black")
        plt.xlabel("Tratamientos")
        plt.ylabel("Tiempo de ensamble [min]")
        plt.show()
        return tabla_lsd
