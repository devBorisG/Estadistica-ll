from math import sqrt

import sympy as sp

x = sp.Symbol('x')


class DatosIntegral:

    def __int__(self, fx, lim_inf, lim_sup, media_poblacional, ex2, var_poblacional, des_estand_poblacional):
        self.fx = fx
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.media_poblacional = media_poblacional
        self.ex2 = ex2
        self.var_poblacional = var_poblacional
        self.des_estand_poblacional = des_estand_poblacional

    @classmethod
    def calculo_integral(cls, fx, lim_inf, lim_sup):
        calculo_integral = cls.__new__(cls)
        calculo_integral.fx = fx
        calculo_integral.lim_inf = lim_inf
        calculo_integral.lim_sup = lim_sup
        calculo_integral.media_poblacional = sp.integrate(fx * x, (x, lim_inf, lim_sup))
        calculo_integral.ex2 = sp.integrate(fx * x ** 2, (x, lim_inf, lim_sup))
        calculo_integral.var_poblacional = calculo_integral.ex2 - (calculo_integral.media_poblacional**2)
        calculo_integral.des_estand_poblacional = sqrt(calculo_integral.var_poblacional)
        return calculo_integral

    def get_fx(self):
        return self.fx

    def get_lim_inf(self):
        return self.lim_inf

    def get_lim_sup(self):
        return self.lim_sup

    def get_media_poblacional(self):
        return self.media_poblacional

    def get_ex2(self):
        return self.ex2

    def get_var_poblacional(self):
        return self.var_poblacional

    def get_des_estand_poblacional(self):
        return self.des_estand_poblacional
