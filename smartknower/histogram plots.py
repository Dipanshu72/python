import matplotlib.pyplot as plt

# #               histogram
# #beans :-equally space regions
# run=[1,24,34,45,56,78,89,103,150]
# plt.hist(run,bins=3)
# plt.show()
# plt.hist(run,bins=[1,30,80,100,120,135,150])
# plt.show()



#customizations of plot

RUNS=[22,44,66,88]
MATCHS=[1,2,3,4]


plt.plot(MATCHS,RUNS)
plt.xlabel('NO OF MATCHS')
plt.ylabel('RUNS SCORED')
plt.yticks([0,25,80,100],['2011','2015','2017','2019'])
plt.title("KOHLI'S PERFORMENCE")

plt.show()