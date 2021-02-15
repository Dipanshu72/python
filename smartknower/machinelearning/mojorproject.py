import pandas as pd
import numpy as np
df=pd.read_csv("D:\python\python\smartknower\ipl2017.csv")
print(df)
print(df.info())
y=df["total"]
x=df.drop("total",axis=1)
X=x.drop(["mid","date"],axis=1)
print(X.head())
print(X.isna().sum())
print(X.dtypes)
X=pd.get_dummies(X,columns=["venue","bat_team","bowl_team","batsman","bowler"])
print(X.dtypes)
print(type(X))
print(X.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print(X.head())

from sklearn.preprocessing import MinMaxScaler #making in same state
scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
print(model.fit(X_train,y_train))

print(model.score(X_test,y_test))

print(model.score(X_train,y_train))





