import numpy as np


class Unifactorial:
    def __init__(self, dataframe):  # Se ingresa el excel
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
        gl_tra = self.k - 1
        gl_t = self.N - 1
        gl_e = self.N - self.k
        self.cm_tra = self.ss_tra / gl_tra  # Varianza para los tratamientos
        self.cmt = self.sst / gl_t  # Varianza total
        self.cme = self.sse / gl_e  # Varianza para el error

    def __suma_totales(self):
        """
    The __suma_totales function is a private function that sums the values of all the columns in a dataframe.
    It takes no arguments and returns an integer value.

    :param self: Allow an object to refer to itself inside of a class
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
