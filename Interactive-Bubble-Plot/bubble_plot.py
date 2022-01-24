from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("factbook.csv")

bi = []
for i in range(0,60,10):
  bi.append(i)
df['Birth Rate'] =(pd.cut(df[' Birth rate'], bins = bi))
df['Population (M)']=(df['Population'].str.replace(',','')).astype(int)
df["GDP per Capita"] = df["GDP per capita"].str.replace(',','').str.replace('$','').astype(float).astype(int)
bubble = sns.scatterplot(data=df, x="GDP per Capita", y="Life expectancy at birth", size="Population (M)", hue="Birth Rate", legend= True, sizes=(10, 300))
bubble.legend()

plt.show()
