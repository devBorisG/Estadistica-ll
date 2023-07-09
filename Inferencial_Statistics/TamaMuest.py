from scipy.stats import norm


class TamaMuest:

    def __int__(self, des_estand_poblacional, nivel_confianza, w, p_gorro):
        """
        The __int__ function is the constructor for this class. It takes in four arguments: des_estand_poblacional =
        The desired standard error of the population proportion (float) nivel_confianza = The confidence level (
        float) w = The weighting factor, which is a function of the confidence level and sample size (float) p_gorro
        = A guess at what you think your population proportion might be. This can be any number between 0 and 1,
        but it's best to use something close to what you expect your actual value will be. If you don't know

    :param self: Represent the instance of the class
    :param des_estand_poblacional: Calculate the standard deviation of the population
    :param nivel_confianza: Calculate the z value
    :param w: Calculate the sample size
    :param p_gorro: Calculate the sample size
    :return: The value of the variable des_estand_poblacional
    :doc-author: Trelent
    """
        self.des_estand_poblacional = des_estand_poblacional
        self.nivel_confianza = nivel_confianza
        self.w = w
        self.p_gorro = p_gorro

    # Creación de instancias de clase dependiendo de la necesidad
    @classmethod
    def tamano_media(cls, des_estand_normal, nivel_confianza, w):
        """
        The tamano_media function calculates the sample size needed to estimate a population mean. The function takes
        three arguments: des_estand_normal: The standard deviation of the population. This is an unknown value,
        so it must be estimated from a previous sample or assumed based on similar populations. nivel_confianza: A
        decimal between 0 and 1 representing how confident you want to be that your results are correct (e.g.,
        95% confidence). Common values for this argument are .90, .95, and .99. w: A decimal representing how much
        error you can tolerate in your results (
    
    :param cls: Create a new instance of the class
    :param des_estand_normal: Calculate the standard deviation of the population
    :param nivel_confianza: Determine the confidence level
    :param w: Calculate the standard deviation of the sample
    :return: A new instance of the tamano_media class
    :doc-author: Trelent
    """
        tamano_media = cls.__new__(cls)
        tamano_media.des_estand_poblacional = des_estand_normal
        tamano_media.nivel_confianza = nivel_confianza
        tamano_media.w = w
        return tamano_media

    @classmethod
    def tamano_proporcion(cls, p_gorro, w, nivel_confianza):
        """
    The tamano_proporcion function is used to calculate the sample size needed for a given proportion.
        The function takes in three arguments: p_gorro, w, and nivel_confianza.
        p_gorro is the expected proportion of successes in the population (e.g., 0.5).
        w is the desired width of our confidence interval (e.g., 0.05).
        nivel_confianza represents our desired level of confidence (e.g., 95%).

    :param cls: Create a new object of the class
    :param p_gorro: Calculate the sample size
    :param w: Calculate the sample size, which is a function of w
    :param nivel_confianza: Define the confidence level of the results
    :return: The sample size for a proportion
    :doc-author: Trelent
    """
        tamano_proporcion = cls.__new__(cls)
        tamano_proporcion.p_gorro = p_gorro
        tamano_proporcion.nivel_confianza = nivel_confianza
        tamano_proporcion.w = w
        return tamano_proporcion

    #%% Creación de getters
    def get_des_estand_poblacional(self):
        """
    The get_des_estand_poblacional function returns the value of the des_estand_poblacional variable.

    :param self: Represent the instance of the class
    :return: The standard deviation of the population
    :doc-author: Trelent
    """
        return self.des_estand_poblacional

    def get_nivel_confianza(self):
        return self.nivel_confianza

    def get_w(self):
        return self.w

    def get_p_gorro(self):
        return self.p_gorro

    #%% Creación de Métodos
    def calcular_tamano_muestra_media(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        z = norm.ppf(alpha_medios)
        n = pow((2 * z * self.get_des_estand_poblacional() / self.get_w()), 2)
        print("El tamaño de la muestra debe ser aproximadamente:", n)

    def calcular_tamano_muestra_proporcion(self):
        alpha = 1 - (self.get_nivel_confianza() / 100)
        alpha_medios = alpha / 2
        z = norm.ppf(alpha_medios)
        n = (4*z**2*((self.get_p_gorro()/100)*(1-(self.get_p_gorro()/100))))/(self.get_w()/100)**2
        print("El tamaño de la muestra debe ser aproximadamente", n)
