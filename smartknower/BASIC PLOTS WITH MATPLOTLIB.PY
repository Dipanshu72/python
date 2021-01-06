import matplotlib.pyplot as plt
runs=[1,24,34,45,56,78,89,103,150]
matchs=[1,2,3,4,5,6,7,8,9]
plt.plot(runs,matchs)
plt.scatter(runs,matchs)

plt.show()

def abc():
    print("-plot-")
    return "returned value/log"
abc()


#               histogram
#beans :-equally space regions
run=[1,24,34,45,56,78,89,103,150]
plt.hist(runs,bins=3)
plt.show()
plt.hist(runs,bins=[1,30,80,100,120,135,150])
plt.show()


