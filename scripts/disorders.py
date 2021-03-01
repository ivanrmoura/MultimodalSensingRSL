import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="whitegrid")
plt.rcParams['legend.fontsize'] = 12
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 400)
import numpy as np

disordes_df = pd.read_csv("../dataset/mental_desorders.csv",sep=';',index_col="idx")
disordes_df['count'] = disordes_df['count'].apply(lambda x: int(x))
print(disordes_df)

# Draw Plot
#fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)

data = disordes_df['count']
categories = disordes_df.index
explode = (0,0,0,0,0,0,0,0,0,0.1)

fig, ax = plt.subplots(figsize=(7, 4), subplot_kw=dict(aspect="equal"))


def func(pct, allvals):
    absolute = pct/100.*np.sum(allvals)
    absolute = np.round(absolute,1)
    absolute = str(absolute)[0:2]
    return "{:.1f}%\n({})".format(pct, absolute)

#return "{:.1f}%\n({:.1f})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, explode=explode,
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(categories[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

#ax.set_title("Mental Disorders and Conditions\n")
plt.savefig('../figure/mental_disoders.png',bbox_inches='tight')
plt.show()

