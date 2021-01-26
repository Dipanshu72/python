import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#eduraka learn
df = pd.read_csv("D:/pokemon.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.columns)
print(df["Type 1"].nunique())
print(df.isnull().sum())
stu=df.drop(['Total'],axis=1)
print(stu)

# relationship analysis

corelation=df.corr()
sns.heatmap(corelation,xticklabels=corelation.columns, yticklabels=corelation.columns,annot=True)
plt.show()
sns.pairplot(df)
plt.show()
sns.relplot(x='Type 1', y='Attack',hue='Type 2',data=df)
plt.show()
sns.displot(df['Type 1'],bins=5)
plt.show()
sns.catplot(x='Type 1',kind='box',data=df)
plt.show()

#bee swarmplot

sns.swarmplot(x='Type 1',y='Attack',data=df)
plt.xticks(rotation=70)
plt.rcParams["ytick.labelsize"]=3
plt.show()







