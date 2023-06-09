import Completely_Random
import pandas as pd

df = pd.read_excel(r'C:\Users\david\Documents\datosunifactorial.xlsx', sheet_name='Hoja1')
var = Completely_Random.Unifactorial(df)

print(var.metodo_lsd_dca())

var.metodo_normalidad_shapiro()

var.prueba_homocedasticidad_bartlett()
