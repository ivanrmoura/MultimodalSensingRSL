import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)

sensors_df = pd.read_csv("../dataset/sensores.csv",sep=';',index_col="idx")
sensors_df = sensors_df.sort_values(by='count')
print(sensors_df)

# this is for plotting purpose
plt.barh( sensors_df.index,sensors_df['count'])
plt.xlabel('Count', fontsize=10)
plt.ylabel('Contextual Data', fontsize=10)
plt.xticks(sensors_df['count'], fontsize=10)
#plt.title('Market Share for Each Genre 1995-2017')
plt.savefig('../figure/count_sensors.png',bbox_inches='tight')
plt.show()

