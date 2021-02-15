#regression tree i work on numeric value.
import pandas as pd

df=pd.read_csv("D:/python/python/smartknower/heart.csv")
print(df.head())

y=df["target"]

# extract Feature

X=df.drop("target",axis=1)
print(X.head())

print(y.isna().sum())

print(X.dtypes)
print(type(X))
print(X.shape)


#2
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
print(X.head())

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(min_samples_leaf=10)
print(model.fit(X_train,y_train))

print(model.score(X_test,y_test))

print(model.score(X_train,y_train))






