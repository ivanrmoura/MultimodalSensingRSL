import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)

inf_geral_df = pd.read_csv("../dataset/info_geral.csv",sep=';')
print(inf_geral_df.sort_values(by='ano',ascending=False))

