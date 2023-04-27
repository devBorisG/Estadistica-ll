import pandas as pd
from scipy import t, norm
import statistics as st
from math import sqrt


class PruebaHipostesisMedia:

    # Definicion de todos los datos nececesarios para todos los casos
    def __init__(self, miu, alfa, x_barra, s, n):
        self.miu = miu
        self.alfa = alfa
        self.x_barra = x_barra
        self.s = s
        self.n = n

    @classmethod
    def hipotesis_media_caso_uno(cls):
        hipotesis_media_caso_uno = cls.__new__(cls)
        # Definición Variables
        return  hipotesis_media_caso_uno

    @classmethod
    def hipotesis_media_caso_dos(cls):
        hipotesis_media_caso_dos = cls.__new__(cls)
        # Definición Variables
        return  hipotesis_media_caso_dos

    @classmethod
    def hipotesis_media_caso_tres(cls):
        hipotesis_media_caso_tres = cls.__new__(cls)
        # Definición Variables
        return hipotesis_media_caso_tres


class PruebaHipotesisProporcion:

    # Definicion de todos los datos necesarios para los casos
    def __init__(self, p_0, p_gorro, n, z, alfa):
        self.p_0 = p_0
        self.p_gorro = p_gorro
        self.n = n
        self.z = z
        self.alfa = alfa

    @classmethod
    def hipotesis_proporcion_valores_p(cls):
        hipotesis_proporcion_valores_p = cls.__new__(cls)
        # Definición Variables
        return hipotesis_proporcion_valores_p

    @classmethod
    def hipotesis_proporcion_valores_z(cls):
        hipotesis_proporcion_valores_z = cls.__new__(cls)
        # Definición Variables
        return hipotesis_proporcion_valores_z
