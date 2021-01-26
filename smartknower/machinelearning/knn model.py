#topic classification model
# 1 Extract feature
#   a. feature and targets should not have any null value 
#   b. feature should be numeric in nature
#   c.feature should be of the type array/ DataFrame
#   d.feature should have some rows and columns
# 2 spilt the dataset into traning and testing datasets
#     a.feature should be on same state
# 3 train model on the traning dataset 
# 4 testing datasets are in testing datasets
import pandas as pd
df = pd.read_csv("D:\python\python\smartknower\Iris.csv")
print(df.head())
y=df["Species"]

# 1 extracting feature
x=df.drop("Species",axis=1)
print(x.head())
p=x.drop("Id",axis=1)
print(p.head())
print(p.isna().sum()) # for check the null value
print(p.dtypes)#for check the numeric value
print(type(p))#for check the array and dataframe
print(p.shape)#having row and column

# 2 split the dataframe
from sklearn.model_selection import train_test_split
p_train,p_test,y_train,y_test = train_test_split(p,y,test_size=0.3,random_state=42,stratify=y)
print(p.head())
print(p.describe())
from sklearn.preprocessing import MinMaxScaler #making in same state
scaler=MinMaxScaler()
p_train=scaler.fit_transform(p_train)
p_test=scaler.transform(p_test)


# 3. for traning data set
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
print(model.fit(p_train,y_train))


#4 for testing data set
print(model.score(p_test,y_test))
