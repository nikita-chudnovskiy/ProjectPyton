import matplotlib.pyplot as plt
import pandas as pd
import seaborn

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

plt.rcParams['figure.figsize'] = (4, 8) # указываем размер визуализации
data =pd.read_csv(r'C:\polomki.csv')
seaborn.heatmap(data)