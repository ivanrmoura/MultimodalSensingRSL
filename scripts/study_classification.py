import pandas as pd
import matplotlib.pyplot as plt
import random
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)

classify_df = pd.read_csv("../dataset/study_classification.csv",sep=';',index_col="idx")
classify_df = classify_df.sort_values(by='count')
#print(classify_df)

#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#langs = ['C', 'C++', 'Java', 'Python', 'PHP']
#students = [23,17,35,29,12]
#plt.bar(classify_df.index,classify_df['count'])
#plt.savefig('../figure/study_classification.png',bbox_inches='tight')

#plt.show()



# Prepare Data
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
df = df_raw.groupby('manufacturer').size().reset_index(name='counts')


#n = classify_df.index.unique().__len__()+1
#all_colors = list(plt.cm.colors.cnames.keys())
#random.seed(100)
#c = random.choices(all_colors, k=n)

# Plot Bars
#plt.figure(figsize=(16,10), dpi= 80)
plt.bar(classify_df.index, classify_df['count'],  width=0.8)#color=c,
for i, val in enumerate(classify_df['count'].values):
    plt.text(i, val, val, horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

# Decoration
plt.gca().set_xticklabels(classify_df.index)
#plt.title("", fontsize=14)
plt.ylabel('Number of studies')
plt.xlabel("Study type")
plt.ylim(0, 16)
plt.savefig('../figure/study_classification.png',bbox_inches='tight')
plt.show()
