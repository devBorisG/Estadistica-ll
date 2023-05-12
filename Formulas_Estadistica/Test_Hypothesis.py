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

from scipy.stats import norm


class Average(object):
    def __init__(self, x_barra: float, miu: float, alpha: float, sigma1: float, sigma2: float, population: int,
                 sample: int, respuesta: str):

        self.x_barra = x_barra
        self.miu = miu
        self.alpha = alpha
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.population = population
        self.sample = sample
        self.respuesta = respuesta

    @classmethod
    def case_l(cls, x_barra: float, population: int, sample: int, sigma1: float, sigma2: float, miu: float,
               alpha: float, option: int):
        """
        The case_l function is used to create an instance of the CaseLWithData class.
        It takes in a number of parameters and returns an object with those parameters as attributes.
        The function also calls the hypothesis_with_z method, which calculates whether Ho should be rejected.

        :param cls: Refer to the class that is being instantiated
        :param x_barra: float: Pass the value of the sample mean
        :param population: int: Represent the population size
        :param sample: int: Determine the sample size
        :param sigma1: float: Calculate the standard deviation of the population
        :param sigma2: float: Calculate the z-score
        :param miu: float: Represent the mean of a population
        :param alpha: float: Determine the alpha level
        :param option: int: User option to appy the test (upper tail [Option 1], lower tail[Option2] or both[Option 3])
        :return: An instance of the class case_l
        :doc-author: David
        """

        def __hypothesis_with_z(self) -> bool:
            """
            The hypothesis_with_z function is used to determine if the null hypothesis should be rejected or not.
            It uses the z-score and compares it with a critical value, which is calculated using the alpha level and
            the cumulative distribution function of a normal distribution. If z &gt; z_alpha, then Ho will be rejected.

            :param self: Allow an instance of a class to refer to itself
            :return: The result of the hypothesis test,
            :doc-author: David
            """
            z = (self.x_barra - self.miu) / (
                math.sqrt(((self.sigma1 ** 2) / self.population) + ((self.sigma2 ** 2) / self.sample)))
            z_alpha = norm.ppf(1 - self.alpha)
            if option is 1:
                if z > z_alpha:
                    return True
                else:
                    return False
            elif option is 2:
                if z < z_alpha:
                    return True
                else:
                    return False
            elif option is 3:
                # TODO: Preguntar como es la decisión en este caso y el calculo
                pass

        case_l = cls.__new__(cls)
        case_l.x_barra = x_barra
        case_l.population = population
        case_l.sample = sample
        case_l.sigma1 = sigma1
        case_l.sigma2 = sigma2
        case_l.miu = miu
        case_l.alpha = alpha
        case_l.respuesta = "Se rechaza Ho" if __hypothesis_with_z(case_l) else "No se rechaza Ho"
        return case_l

    @classmethod
    def case_ll(cls, x_barra: float, population: int, sample: int, sigma1: float, sigma2: float, miu: float,
                alpha: float, option: int):
        pass
