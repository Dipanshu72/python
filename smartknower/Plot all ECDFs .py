import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
values=[11,22,33,44,55]
def ecdf(data):
    x=np.sort(data)
    y=np.arange(1,len(data)+1)/len(data)
    return x,y
x_values,y_values=ecdf(values)
plt.scatter(x_values,y_values)
plt.show()
print(np.mean(values))