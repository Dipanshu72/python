import pandas


#data frames using dictionary
df=pandas.DataFrame({'Hotel items':['pizza','biryani','sandwich'],'Price':[350,140,60],'Discount':[5,3,2]})
#print(df)


da=pandas.read_csv("D:\machine learning\python\sampleIPL.csv")
print(da)
print(da.head(2)) #for the number of column

#subset the column
print(da["team"])

#subset consecutive rows
print(da[1:3])

#sunsetting column loc=label name and iloc=label index
print(da.iloc[[1,3] ,1])

#sunsetting with condition

#1.1convert into boolean
print(da["score"]>100)

print(da[da["score"]>100])

#subsetting the multiple condition
print(da[(da["score"]>100) & (da["score"]<300)])

#reset row level into colum and vise vsera
#row label to column->reset_index
#column to row label->set_index

print(da.set_index("score"))
print(da.reset_index())

print(da.sort_values("score",ascending=False))

print(da.sort_values(["score","match"]))
print(da.sort_values(["score","match"],ascending=[False,True]))