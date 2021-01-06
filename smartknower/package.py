from math import*
print(radians(12))
#import math as mt ( for rname the method)
# print(math.radian(12))
#from math import radians(for only radians)


# for numpy
height = [1.72,136.3,456.5,782.3,68.5]
print(height)
weight = [12,35,65,85,96]
print(weight)
import numpy as np
np_height =np.array(height)
print(np_height)

np_weight=np.array(weight)
print(np_weight)

bmi=np_weight/np_height **2
print(bmi)

print(np.array("abc"))

a=[1,2,5]
b=[2,2,5]
print(a+b)
a_new=np.array(a)
b_new=np.array(b)
print(a_new+b_new)








# class 5



import numpy as np
a= np.array([11,22,33,44])
print(a)
print(a[2])
print(a[1:3])


# 2d array

np_2d = np.array([[11,22,33,44,66],[77,88,66,33,55]])
print(np_2d)
print(np_2d.shape)
print(np_2d[:,1:3])
