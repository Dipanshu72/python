import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#variance
values=[11,22,33,44,55]
mea=np.mean(values)
print(mea)
distance=values-mea
print(distance)
square_distance=distance**2
print(square_distance)
SOSD=square_distance.sum()
print(SOSD)
print(SOSD/len(values))
print(np.var(values))
print(np.sqrt(SOSD/len(values)))