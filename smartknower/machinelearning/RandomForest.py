# step1-create abootstrap dataset
#       take the feature colum and to same ramdom selct the row
# step2-create a decision tree using the bootstrapped dataset,but only use a rondom subset of variable(or column) at each step     
# bagging = dataset which are not in use
import pandas as pd

import numpy as np
df=pd.read_csv("D:/python/python/smartknower/house-votes-84.csv")
print(df)
print(df.isna().sum())
df.replace("?",np.nan,inplace=True)
print(df)
print(df.isna().sum())
print(df.shape)

# subset your column of intrest
# convert it to boolean based on condition
# surround with varuiableName[..code uptil step 2..]

republican=df[df["Class Name"]=="republican"]
democrat=df[df["Class Name"]=="democrat"]
print(republican.shape)
print(democrat.shape)
#for fill the column 

for columnName in republican.columns:
    republican[columnName]=republican[columnName].fillna(republican[columnName].mode()[0])

print(republican.isna().sum())

for columnName in democrat.columns:
    democrat[columnName]=democrat[columnName].fillna(democrat[columnName].mode()[0])

print(democrat.isna().sum())


# joining the column
data=pd.concat([republican,democrat],axis=0)
print(data.shape)
y=df["Class Name"]

x=data.drop("Class Name",axis=1)
print(x.head())
print(x.isna().sum())
print(x.dtypes)

X=pd.get_dummies(x,columns=x.columns)
print(X.dtypes)
print(type(X))
print(X.shape)


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=40,stratify=y)
print(X.head())



from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=150,oob_score=True)

print(model.fit(X_train,y_train))

print(model.score(X_test,y_test))

print(model.oob_score_)