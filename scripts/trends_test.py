import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
sns.set_context("notebook", font_scale=1.1, rc={"lines.linewidth": 3.5})
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)

df = pd.read_csv("../dataset/trends_teste.csv", sep=';')


df.set_index('year').plot(kind='bar', stacked=True)
plt.xlabel("Years")
plt.ylabel("Number of studies")
plt.savefig('../figure/trends.png',bbox_inches='tight')
plt.show()
