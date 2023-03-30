from math import sqrt

from scipy.stats import norm, chi2


# Z
def teorema_limite_central(x_barra, miu, sigma, n):
    return (x_barra - miu) / (sigma / sqrt(n))


def desviacion_estandar_tipica_media(sigma, n):
    return sigma / sqrt(n)


def probabilidad_z_menores(z):
    return norm.cdf(float(z), 0, 1)


def probabilidad_z_mayores(z):
    return 1 - norm.cdf(float(z), 0, 1)


# CHI CUADRADO
def teorema_varianza(n, s2, sigma2):
    return ((n - 1) * s2) / sigma2


def probabilidad_chi2_menores(chi_2, n):
    return chi2.pdf(chi_2, n - 1)


def probabilidad_chi2_mayores(chi_2, n):
    return 1 - chi2.pdf(chi_2, n - 1)


def desviacion_estandar_tipica_varianza_muestral(sigma, n):
    return sigma / sqrt(n - 1)


# Z
def teorema_proporcion(p_gorro, p, n):
    p_gorro = p_gorro / 100
    p = p / 100
    q = 1-p
    return (p_gorro - p) / (sqrt((p * q / n)))


def desviacion_estandar_proporcion(p, n):
    return sqrt(p * (1 - p) / n)
