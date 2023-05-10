from itertools import combinations

import pandas as pd


# %%Tabla de muestreo
def tabla_muestreo(data):
    """
    Realiza todas las combinaciones posibles de los datos, calculando la media muestral y
    la varianza muestral.
    :param data: DataFrame
    :return: DataFrame
    """
    dates = []  # Iran contenidos todos los datos
    temp = combinations(data, 2)  # Encontramos todas las combinaciones posibles
    for i, j in temp:
        empleados = f"{i} {j}"
        anos_experiencia = (data[i][0], data[j][0])  # Busca los datos parecidos entre las dos tablas, adiciona su valor
        media_muestral = (data[i][0] + data[j][0]) / 2  # Cálculo de la media muestral
        varianza_muestral = sum((item - media_muestral) ** 2 for item in anos_experiencia)  # Calculo varianza muestral
        dates.append(pd.Series([empleados,
                                anos_experiencia,
                                media_muestral,
                                varianza_muestral],
                               index=['Empleados',
                                      'Años_Experiencia',
                                      'Media',
                                      'Varianza_Muestral']))  # Se agregan todos datos a la lista
    df_muestreo = pd.DataFrame(dates, index=range(1, len(dates) + 1))  # Se adicionan los datos a un DataFrame
    return df_muestreo


# %%Distribución de probabilidad
def distri_prob(tb_mb):
    """
    Calcula las medias repetidas, encuentra su frecuencia y su frecuencia relativa.
    :param tb_mb: DataFrame
    :return: DataFrame
    """
    dates = []
    lista = tb_mb.Media.drop_duplicates()  # Se eliminan datos duplicados
    for item in lista:
        media = item
        frecuencia = int(list(tb_mb.Media).count(item))  # Se calcula la frecuencia
        fr = round(frecuencia / len(tb_mb), 4)  # Se calcula la frecuencia relativa con cuatro decimales
        percent = str(round(fr * 100, 2)) + " %"  # Se convierte la FR a porcentaje con dos decimales
        dates.append(pd.Series([media,
                                frecuencia,
                                fr,
                                percent],
                               index=['Media',
                                      'Frecuencia',
                                      'F.R',
                                      'Porcentaje']))  # Se agregan los datos a la lista
    df_dis_prob = pd.DataFrame(dates, index=range(1, len(lista) + 1))  # Se adicionan los datos a un DataFrame
    return df_dis_prob


# %%Distribución de probabilidad varianza
def distri_prob_var(tb_mb):
    """
    Ordena de forma ascendente en función de la varianza muestral, calcula las varianzas repetidas,
    encuentra su frecuencia y su frecuencia relativa.
    :param tb_mb: DataFrame
    :return: DataFrame
    """
    tb_mb = tb_mb.sort_values('Varianza_Muestral')  # Se organizan los datos ascendentes para la varianza muestral
    dates = []
    lista = tb_mb.Varianza_Muestral.drop_duplicates()  # Elimina datos duplicados
    for item in lista:
        varianza = item
        frecuencia = int(list(tb_mb.Varianza_Muestral).count(item))
        fr = round(frecuencia / len(tb_mb), 4)  # Se calcula la frecuencia relativa con cuatro decimales
        percent = str(round(fr * 100, 2)) + " %"  # Se convierte la FR a porcentaje con dos decimales
        dates.append(pd.Series([varianza,
                                frecuencia,
                                fr,
                                percent],
                               index=['Varianza Muestral',
                                      'Frecuencia',
                                      'F.R',
                                      'Porcentaje']))  # Se agregan los datos a la lista
    df_dis_prob_var = pd.DataFrame(dates, index=range(1, len(lista) + 1))  # Se adicionan los datos a un DataFrame
    return df_dis_prob_var


# %% Ingreso de información
# Creación de los datos años de los empleados para poder hallar una tabla de muestreo
# Entre una combinación de 2 empleados y también encontrar la distribución de probabilidad
# y la distribución de probabilidad de la varianza.

data = pd.DataFrame({'E1': [2],
                     'E2': [4],
                     'E3': [6],
                     'E4': [6],
                     'E5': [7],
                     'E6': [8]})  # Ingreso de los años de los empleados

tb_m = tabla_muestreo(data)
dis_prob = distri_prob(tb_m)
dis_prob_var = distri_prob_var(tb_m)
