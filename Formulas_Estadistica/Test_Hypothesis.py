"""
Pasos Generales

1. Identificar el parámetro de interés (Ejemplo: Media)
2. Establecer hipótesis nula Ho
3. Especificar una hipótesis alternativa apropiada, Ha
4. Elegir un nivel de significancia "alpha"
5. Establecer un estadístico de prueba apropiado
6. Establecer una región de rechazo estadístico
7. Calcular las cantidades muestrales necesarias, sustituirlas en la ecuación del estadístico de prueba y calcular ese
    valor
8. Decidir si se debe rechazar o no Ho y contextualizar la decisión del problema
"""
import math
from statistics import mean

from scipy.stats import norm


class Average(object):
    def __init__(self, x_barra: float, miu: float, alpha: float, sigma1: float, sigma2: float, population: int,
                 sample: int):

        self.x_barra = x_barra
        self.miu = miu
        self.alpha = alpha
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.population = population
        self.sample = sample

    @classmethod
    def case_l_with_data(cls, data: list, sample: int, sigma1: float, sigma2: float) -> object:
        """
        The case_l_with_data function is a class method that creates an instance of the case_l class.
        It takes in four arguments: data, sample, sigma 1 and sigma 2. The data argument is a list of numbers
        hat represent the population from which we will take our sample. The sample argument represents how many
        numbers we want to take from our population (sample size). Sigma 1 and sigma 2 are two different standard deviations
        of the same normal distribution.

        :param cls: Create a new instance of the class
        :param data: list: Pass the data to the class
        :param sample: int: Specify the sample size
        :param sigma1: float: Set the value of the sigma_one attribute
        :param sigma2: float: Calculate the standard deviation of the sample
        :return: An object of class case_l
        :doc-author: David
        """
        case_l_with_data = cls.__new__(cls)
        case_l_with_data.x_barra = mean(data)
        case_l_with_data.population = len(data)
        case_l_with_data.sample = sample
        case_l_with_data.sigma1 = sigma1
        case_l_with_data.sigma2 = sigma2
        return case_l_with_data

    def hypothesis_with_z(self):
        z = (self.x_barra - self.miu) / (
            math.sqrt(((self.sigma1 ** 2) / self.population) + ((self.sigma2 ** 2) / self.sample)))
        z_alpha = norm.ppf(1 - self.alpha)
        if z > z_alpha:
            return "Se rechaza Ho"
        else:
            return "No se rechaza Ho"
