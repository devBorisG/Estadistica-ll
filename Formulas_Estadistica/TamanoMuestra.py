from scipy.stats import norm


class TamanoMuestra:

    def __int__(self, des_estand_poblacional, nivel_confianza, w, p_gorro):
        self.des_estand_poblacional = des_estand_poblacional
        self.nivel_confianza = nivel_confianza
        self.w = w
        self.p_gorro = p_gorro

    # Creación de instancias de clase dependiendo de la necesidad
    @classmethod
    def tamano_media(cls, des_estand_normal, nivel_confianza, w):
        tamano_media = cls.__new__(cls)
        tamano_media.des_estand_poblacional = des_estand_normal
        tamano_media.nivel_confianza = nivel_confianza
        tamano_media.w = w
        return tamano_media

    @classmethod
    def tamano_proporcion(cls, p_gorro, w, nivel_confianza):
        tamano_proporcion = cls.__new__(cls)
        tamano_proporcion.p_gorro = p_gorro
        tamano_proporcion.nivel_confianza = nivel_confianza
        tamano_proporcion.w = w
        return tamano_proporcion
    #%% Creación de getters
    def get_des_estand_poblacional(self):
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
        n = (4*z**2*((self.get_p_gorro()/100)*(1-(self.get_p_gorro()/100))))/(self.get_w())**2
        print("El tamaño de la muestra debe ser aproximadamente", n)
