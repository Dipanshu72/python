import pandas as pd
df=pd.read_csv("D:/python/python/smartknower/heart.csv")
print(df.head())

y=df["target"]
x=df.drop("target",axis=1)
print(x.head())

X=x.drop("sex",axis=1)
print(X.head())
print(X.isna().sum())
print(X.dtypes)
print(type(X))
print(X.shape)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
print(X.head())
print(X.describe())
from sklearn.preprocessing import MinMaxScaler #making in same state
scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
print(model.fit(X_train,y_train))
print(model.score(X_test,y_test))

