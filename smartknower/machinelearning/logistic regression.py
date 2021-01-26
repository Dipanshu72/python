#1.convert y-axis to probality
#2.convert y-asix to log of odds
 #          i.e=log(p/1-p)
 #3.take a random straight line
#4.convert y-axis to prob again
        #i.e p=e^log(odds)/1+e^log(odds)

# r^2=log(over prob)-log(fit)/log(over prob)
import pandas as pd 
df= pd.read_csv('D:/python/python/smartknower/train.csv')
print(df.head())

y=df["Survived"]

x=df.drop("Survived",axis=1)
print(x)
p=x.drop(["PassengerId","Name","Ticket","Embarked"],axis=1)
print(p.head())

print(p.isna().sum())
print(p.shape)
g=p.drop("Cabin",axis=1)
print(g.head())
print(g.isna().sum())

#fill
g["Age"]=g["Age"].fillna(g["Age"].mean())
print(g.isna().sum())
print(g.dtypes)

c=pd.get_dummies(g,columns=["Sex"],drop_first=True)
print(c.dtypes)

print(type(c))
print(c.shape)


#2
from sklearn.model_selection import train_test_split
c_train,c_test,y_train,y_test=train_test_split(c,y,random_state=42,stratify=y)
print(c.head())

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
c_train=scaler.fit_transform(c_train)
c_test=scaler.transform(c_test)


#3
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
print(model.fit(c_train,y_train))

#4
print(model.score(c_test,y_test))


#predication
data=pd.DataFrame({"first":[7],"second":[1],"Third":["Rohan Waleker"],"fourth":["female"],"fifth":[222],"sixth":[2],"seventh":[0],"eigth":["AC 34343"],"ninth":[71],"tenth":["C324"],"eleventh":["S"]})
print(data)
f=data.drop(["first","Third","eigth","tenth","eleventh"],axis=1)
print(f)
q=pd.get_dummies(f,columns=["fourth"])
q.loc[0,"fourth_female"]=0
print(q)
q=scaler.transform(q)
print(model.predict(q))





