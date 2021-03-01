import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)


# Import Dataset
#df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

df = pd.read_csv("../dataset/combinacao_comportamentos.csv",sep=';')
print(df)

# Plot
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(df, xticklabels=df.columns, yticklabels=df.columns,
            cmap='RdYlGn', center=0, annot=True, cbar=False)

# Decorations
#plt.title('Behaviors combination', fontsize=22)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.savefig('../figure/comb_behavior.png',bbox_inches='tight')
plt.show()