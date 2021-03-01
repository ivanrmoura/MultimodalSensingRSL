import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)

behaviors_df = pd.read_csv("../dataset/comportamentos.csv",sep=';',index_col="idx")
behaviors_df = behaviors_df.sort_values(by='count')
print(behaviors_df)

# this is for plotting purpose
plt.barh( behaviors_df.index,behaviors_df['count'])
plt.xlabel('Count', fontsize=10)
plt.ylabel('Behaviors', fontsize=10)
plt.xticks(behaviors_df['count'], fontsize=10)
#plt.title('Market Share for Each Genre 1995-2017')
plt.savefig('../figure/count_behaviors.png',bbox_inches='tight')
plt.show()

