import pandas as pd 
df=pd.read_csv("D:\python\python\smartknower\gapminder.csv")
print(df.head())

y=df["fertility"]
x=df.drop("fertility",axis=1)
print(x.head())
print(x.isna().sum())
print(x.dtypes)

x=pd.get_dummies(x,columns=["Region"])
print(x.head())
print(x.dtypes)
print(type(x))
print(x.shape)

from sklearn.model_selection import  train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(x.head())

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit(x_test)


from sklearn.tree import DecisionTreeRegressor

model=DecisionTreeRegressor(min_samples_leaf=6)

print(model.fit(x_train,y_train))

print(model.score(x_test,y_test))
