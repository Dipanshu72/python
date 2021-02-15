# 1.select the number of cluster you want to identify in your data. this is the K in k mean clustring
# 2.select randomly 3 distinct data points.
# 3.measure the distnce between the 1st point and the three initial clusters.
# 4.assign the 1st point to the nearest cluster.in this case thee nearest cluster is the blue cluster.
# 5.calculate the mean of the each cluster

import pandas as pd 
df=pd.read_csv("D:/python/python/smartknower/Country-data.csv")
print(df)

# in unsupervised learning
# 1.ecxtract feature
#    a.feature  should not have null values
#    b.features shoul br numeruc in nature
#    c.feature should be of type array and DataFrame
#    d.feature should have some rows and column
#    e.feature should be on same scale
# 2.train the model on the entire  dataset

x=df
print(x.head())
X=x.drop("country",axis=1)
print(X.head())
print(X.isna().sum())
print(X.dtypes)
print(type(X))

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

X=scaler.fit_transform(X)


from sklearn.cluster import KMeans
spread=[]
for clusterNumber in [2,3,4,5,6,7,8,9,10]:
    model=KMeans(n_clusters=clusterNumber)
    model.fit(X)
    spread.append(model.inertia_)
print(spread) 


import matplotlib.pyplot as plt

plt.plot([2,3,4,5,6,7,8,9,10],spread)
#plt.show()


#so at 7, we get very less reduction variance
model=KMeans(n_clusters=7)
print(model.fit(X))

predictions=model.predict(X)
predictions=pd.DataFrame(predictions)
print(predictions)
predictions.columns=["ClusterId"]
print(predictions)
data=pd.concat([predictions,df],axis=1)
print(data)

# 1.subset your column on intrest
# 2.convert it to boolean on condition
# 3.surround it with variableaName[..code uptil stpe 2..]

print(data[data["ClusterId"]==0]["country"].values)
print(data[data["ClusterId"]==1]["country"].values)
print(data[data["ClusterId"]==2]["country"].values)
print(data[data["ClusterId"]==3]["country"].values)
print(data[data["ClusterId"]==4]["country"].values)
print(data[data["ClusterId"]==5]["country"].values)
print(data[data["ClusterId"]==6]["country"].values)








