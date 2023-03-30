from itertools import combinations, product

import pandas as pd


class DistriMuestre:

    def __int__(self, datos, x_barra, var_poblacional, combinaciones, tb_mues, tb_dis_prob, tb_prob_var):
        self.datos = datos
        self.x_barra = x_barra
        self.var_poblacional = var_poblacional
        self.combinaciones = combinaciones
        self.tb_mues = tb_mues
        self.tb_dis_prob = tb_dis_prob
        self.tb_prob_var = tb_prob_var

    @classmethod
    def creacion_tablas_permutacion(cls, datos, combinaciones):
        creacion_tablas = cls.__new__(cls)
        creacion_tablas.datos = datos
        creacion_tablas.x_barra = float(datos.mean(axis=1))
        creacion_tablas.var_poblacional = float(datos.var(axis=1,
                                                          ddof=0))  # axis=1 quiere decir la fila 1, ddof=0 (varianza
        # poblacional), ddof=1 (varianza muestral, esta como predeterminado)
        creacion_tablas.combinaciones = combinaciones
        creacion_tablas.tb_mues = DistriMuestre.tabla_muestreo_permutacion(creacion_tablas)
        creacion_tablas.tb_dis_prob = DistriMuestre.tabla_distri_probabilidad(creacion_tablas)
        creacion_tablas.tb_prob_var = DistriMuestre.tabla_distri_probabilidad_varianza(creacion_tablas)
        return creacion_tablas

    @classmethod
    def creacion_tablas_combinacion(cls, datos, combinaciones):
        creacion_tablas = cls.__new__(cls)
        creacion_tablas.datos = datos
        creacion_tablas.x_barra = float(datos.mean(axis=1))
        creacion_tablas.var_poblacional = float(datos.var(axis=1,
                                                          ddof=0))  # axis=1 quiere decir la fila 1, ddof=0 (varianza
        # poblacional), ddof=1 (varianza muestral, esta como predeterminado)
        creacion_tablas.combinaciones = combinaciones
        creacion_tablas.tb_mues = DistriMuestre.tabla_muestreo_combinatoria(creacion_tablas)
        creacion_tablas.tb_dis_prob = DistriMuestre.tabla_distri_probabilidad(creacion_tablas)
        creacion_tablas.tb_prob_var = DistriMuestre.tabla_distri_probabilidad_varianza(creacion_tablas)
        return creacion_tablas

    # Creación de getters
    def get_x_barra(self):
        return self.x_barra

    def get_var_poblacional(self):
        return self.var_poblacional

    def get_datos(self):
        return self.datos

    def get_combinaciones(self):
        return self.combinaciones

    def get_tabla_muestreo(self):
        return self.tb_mues

    def get_dis_tabla_prob(self):
        return self.tb_dis_prob

    def get_prob_var(self):
        return self.tb_prob_var

    # Creación de comportamientos
    def tabla_muestreo_permutacion(self):
        dates = []
        temp = product(self.get_datos(), repeat=self.get_combinaciones())
        for i, j in temp:  # Se agregan o se quitan iteraciones (i,j,k,...) dependiendo de cuantas combinaciones
            # soliciten
            datos = f"{i} {j}"
            valor_datos = (self.get_datos()[i][0], self.get_datos()[j][0])
            media_muestral = (self.get_datos()[i][0] + self.get_datos()[j][0]) / self.get_combinaciones()
            varianza_muestral = sum((item - media_muestral) ** 2 for item in valor_datos) / (len(valor_datos) - 1)
            dates.append(pd.Series([datos,
                                    valor_datos,
                                    media_muestral,
                                    varianza_muestral],
                                   index=['Datos',
                                          'Valor_Datos',
                                          'Media_Muestral',
                                          'Varianza_Muestral']))
        df_muestreo = pd.DataFrame(dates, index=range(1, len(dates) + 1))
        return df_muestreo

    def tabla_muestreo_combinatoria(self):
        dates = []
        temp = combinations(self.get_datos(), self.get_combinaciones())
        for i, j, k in temp:  # Se agregan o se quitan iteraciones (i,j,k,...) dependiendo de cuantas combinaciones
            # soliciten
            datos = f"{i} {j} {k}"
            valor_datos = (self.get_datos()[i][0], self.get_datos()[j][0], self.get_datos()[k][0])
            media_muestral = (self.get_datos()[i][0] + self.get_datos()[j][0] + self.get_datos()[k][0]) / self.get_combinaciones()
            varianza_muestral = sum((item - media_muestral) ** 2 for item in valor_datos) / (len(valor_datos) - 1)
            dates.append(pd.Series([datos,
                                    valor_datos,
                                    media_muestral,
                                    varianza_muestral],
                                   index=['Datos',
                                          'Valor_Datos',
                                          'Media_Muestral',
                                          'Varianza_Muestral']))
        df_muestreo = pd.DataFrame(dates, index=range(1, len(dates) + 1))
        return df_muestreo

    def tabla_distri_probabilidad(self):
        dates = []
        lista = self.get_tabla_muestreo().Media_Muestral.drop_duplicates()
        for item in lista:
            media = item
            frecuencia = int(list(self.get_tabla_muestreo().Media_Muestral).count(item))
            fr = round(frecuencia / len(self.get_tabla_muestreo()), 4)  # Cuatro decimales de precisión
            percent = str(round(fr * 100, 2)) + " %"  # Conversión a porcentaje
            dates.append(pd.Series([media,
                                    frecuencia,
                                    fr,
                                    percent],
                                   index=['Media',
                                          'Frecuencia',
                                          'F.R',
                                          'Porcentaje']))
        df_dis_prob = pd.DataFrame(dates, index=range(1, len(lista) + 1))
        return df_dis_prob

    def tabla_distri_probabilidad_varianza(self):
        tmb = self.get_tabla_muestreo().sort_values('Varianza_Muestral')
        dates = []
        lista = tmb.Varianza_Muestral.drop_duplicates()
        for item in lista:
            varianza = item
            frecuencia = int(list(tmb.Varianza_Muestral).count(item))
            fr = round(frecuencia / len(tmb), 4)
            percent = str(round(fr * 100, 2)) + " %"
            dates.append(pd.Series([varianza,
                                    frecuencia,
                                    fr,
                                    percent],
                                   index=['Varianza Muestral',
                                          'Frecuencia',
                                          'F.R',
                                          'Porcentaje']))
        df_dis_prob_var = pd.DataFrame(dates, index=range(1, len(lista) + 1))
        return df_dis_prob_var
