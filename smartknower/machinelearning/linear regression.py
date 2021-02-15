#calculate variance.
   #1.calculate distance with respect to a refrence line(usually reference line is at the mean)
   #2.square the distance
   #3.sum all the squared distance
   #4.divide by total no. of point
   #var= sum of square distance/number of points
# r^2=var(mean)-var(fit)/var(mean)

import pandas as pd
df=pd.read_csv("D:\python\python\smartknower\gapminder.csv")
print(df.head())
y=df["fertility"]

x=df.drop("fertility",axis=1)
print(x.head())
print(x.isna().sum())
print(y.isna().sum())
print(x.dtypes)
print(x["Region"].unique())
p=pd.get_dummies(x,columns=["Region"],drop_first=True)
print(p)
print(type(p))

from sklearn.model_selection import train_test_split
p_train,p_test,y_train,y_test=train_test_split(p,y,test_size=0.3,random_state=42)
print(p.head())

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
p_train=scaler.fit_transform(p_train)
p_test=scaler.transform(p_test)


#3
from sklearn.linear_model import LinearRegression
model=LinearRegression()
print(model.fit(p_train,y_train))


#4
print(model.score(p_test,y_test))

#pridict
print(p.head())
data=pd.DataFrame({"First":[100],"Second":[0.7],"Third":[55],"Fourth":[30],"Fifth":[12000],"Sixth":[200],"Seventh":[70],"Eigth":[130],"Ninth":[0],"Tenth":[0],"Eleventh":[0],"Twelve":[1],"Thirtheen":[0]})
print(p.shape)
print(data.shape)
print(data)
scaler.transform(data)
print(model.predict(data))