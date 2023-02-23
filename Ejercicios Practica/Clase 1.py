import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib import colors

data = pd.DataFrame({'Fuera de perfil': [30, 37.037, 37.07],
                     'Piezas desordenadas': [21, 25.926, 62.963],
                     'Agujero': [6, 7.407, 70.370],
                     'Fuera de secuencia': [6, 7.407, 77.778],
                     'Partes no lubricadas': [5, 6.173, 83.951]})