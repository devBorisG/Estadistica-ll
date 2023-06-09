import Completely_Random
import pandas as pd

df = pd.read_excel(r'C:\Users\david\Documents\datosunifactorial.xlsx', sheet_name='Hoja1')
var = Completely_Random.Unifactorial(df).cm_tra
print(var)
