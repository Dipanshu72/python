import pandas as pd
df= pd.read_csv("D:/python/python/smartknower/TrumpTrudeau.csv")
print(df.head())

y=df["author"]

x=df["status"]

print(x.isna().sum())
print(y.isna().sum())

print(x.dtypes)


#               string 
#               /     \ 
#        categorial   continous
#         (finite)      (infinite)
#        /    \              /   \
#   one-not    dummy     Tf-idf    count
#   encoding    encoding vectorial   vectorial


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)

from sklearn.feature_extraction.text import CountVectorizer
CountVectorizer=CountVectorizer(stop_words="english")
x_train=CountVectorizer.fit_transform(x_train)
x_test=CountVectorizer.transform(x_test)

print(type(x_test))

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()

print(model.fit(x_train,y_train))
print(model.score(x_test,y_test))

print(df.shape)
#predict
tweet="his is an archive of a Trump Administration account, maintained by the National Archives and Records Administration."
data=CountVectorizer.transform([tweet])
print(model.predict(data))


