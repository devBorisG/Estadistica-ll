import numpy as np
from itertools import combinations
from scipy.stats import t, f, shapiro, bartlett
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import pandas as pd


class Unifactorial:
    def __init__(self, dataframe: pd.DataFrame):  # Se ingresa el excel
        """
    The __init__ function is the constructor of the class. It initializes all the attributes that are needed for
    the rest of the functions to work properly. The dataframe attribute is initialized with whatever dataframe was
    passed to it when creating an instance of this class.

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
        # Calculamos y añadimos la columna de totales a nuestra matriz
        self.dataframe["Total"] = self.dataframe[1]+self.dataframe[2]+self.dataframe[3]+self.dataframe[4]
        # de datos
        self.totales = self.dataframe["Total"].tolist()  # Convertimos la columna de totales en una lista
        self.y_total = sum(self.dataframe["Total"])  # Calculamos "y. ." Sumando los elementos de la columna de totales
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
    The metodo_lsd_dca function takes the dataframe and calculates the L.S.D method for DCA.
        It returns a table with the pairs of means, their difference and if they are significant or not.

    :param self: Represent the instance of the class
    :return: A table with the results of the l.s.d method
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

    def metodo_normalidad_shapiro(self):
        """
    The metodo_normalidad_shapiro function is used to test the normality of the residuals.
        It uses a Shapiro Wilks test and a graphical method to determine if the residuals are normally distributed.
        The function prints out whether we can reject normality, as well as an R2 value for the graphical method.

    :param self: Represent the instance of the class
    :return: The following values:
    :doc-author: David
    """
        data_normal = pd.DataFrame()
        data_normal["Data"] = self.__data_normal_to_list()  # 1. Necesitamos una lista con todos los datos de matriz
        # del DDE
        shapiro_value = shapiro(data_normal["Data"])  # 2. Se realiza la prueba de shapiro Wilks con la función
        # Shapiro de scipy
        print("El valor de W calculado es:", shapiro_value[0])  # Se imprime el valor de W calculado y el valor P
        print("El valor P para el W calculado de la prueba de shapiro es:", shapiro_value[1])
        if shapiro_value[1] < 0.05:
            print("Se rechaza normalidad de los residuos")
        else:
            print("No se rechaza normalidad de los residuos, el ANOVA es valido en cuestión de normalidad")

        # Prueba gráfica de normalidad
        # 1. Se necesitan los datos en una sola columna
        # 2. Se organiza los datos en orden ascendente
        data_normal = data_normal.sort_values("Data")
        # 3. Se le asigna a cada dato un posición
        i = list(range(1, len(data_normal)+1))  # Se crea una lista con las posiciones
        data_normal["i"] = i  # Se anexan las posiciones al DataFrame
        # 4. Se calcula el papel de probabilidad normal

        def normal_operation(value):
            """
        The normal_operation function takes a value and returns the normalized value.
            The normalization is done by subtracting 0.05 from the inputted value, then dividing that result by N.

        :param value: Calculate the normal operation of the system
        :return: The value of the normal operation
        :doc-author: David
        """
            return (value - 0.05)/self.N

        data_normal["(i-0.5)/N"] = data_normal["i"].apply(lambda item: normal_operation(item))
        plt.plot(data_normal["Data"], data_normal["(i-0.5)/N"], "bo")
        plt.xlabel("ri")
        plt.ylabel("(i-0.05)/N")
        plt.show()

        # Sacar R2 de la prueba de normalidad gráfica
        x = np.array(data_normal["Data"]).reshape(-1, 1)
        y = np.array(data_normal["(i-0.5)/N"]).reshape(-1, 1)
        regression = LinearRegression().fit(x, y)
        print("El R2 de la regresión es:", regression.score(x, y))

    def __data_normal_to_list(self):
        """
    The __data_normal_to_list function takes the dataframe and converts it into a list.
        This is done by taking each column of the dataframe, converting it to a list, and then appending that
        list to an empty value variable.
        The function returns this value variable.

    :param self: Represents the instance class
    :return: A list of all the values in the dataframe
    :doc-author: David
    """
        value = []
        for i in range(1, self.k+1):
            value += self.dataframe[i].tolist()
        return value

    def prueba_homocedasticidad_bartlett(self):
        data_tras = self.dataframe.transpose()  # 1. Se transpone la matriz, dado que la libreria pide los datos en
        # forma de columna, es decir cada tratamiento va a ser una columna y no una fila
        data_tras = data_tras.drop(["medias", "Total"])  # 2. Se quita las filas de medias y totales, solo se requieren
        # los datos
        barlett_test = bartlett(data_tras[0], data_tras[1], data_tras[2], data_tras[3])  # Se meten los datos en la
        # función de barlett para la prueba de homocedasticidad
        print("EL valor de chi cuadrado calculado es:", barlett_test[0])
        print("El valor de P para prueba de Barlett es:", barlett_test[1])
        if barlett_test[1] < 0.05:
            print("Se rechaza Homocedasticidad, por lo tanto el ANOVA no es valido")
        else:
            print("No se rechaza Homocedasticidad, el ANOVA es valido")

        # Prueba gráfica de homocedasticidad "Varianza constante"
        residuos = []
        for i in range(self.n):
            predicho = self.dataframe["medias"][i]
            residuo = data_tras[i]-predicho
            residuos.append(residuo)
            plt.plot([predicho, predicho, predicho, predicho], residuo, "bo")
        plt.show()
