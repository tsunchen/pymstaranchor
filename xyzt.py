#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/05/08 22:10
@upgrade:
"""

import pandas as pd
from pandas import DataFrame

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename_0505 = 'e:/xyz/20180508_200b.txt'


file = filename_0505
f3 = pd.read_table(file, engine="python", skiprows=[0,1], header=None, sep=":")[2]
lenf3 = len(f3)

fd3=[]
fd4=[]
fd5=[]
for j in range(lenf3):
    f3 = int(pd.read_table(file, engine="python", skiprows=[0,1], header=None, sep=":")[2][j][8])
    fd3.append(f3)
    f4 = int(pd.read_table(file, engine="python", skiprows=[0,1], header=None, sep=",")[1][j])
    fd4.append(f4)
    f5 = int(pd.read_table(file, engine="python", skiprows=[0,1], header=None, sep=":")[2][j][12])
    fd5.append(f5)
    
p = DataFrame([fd3,fd4,fd5])

PE = p.T
PE.columns = ['X','Y','Z']
#print (PE)
print (PE.describe())

'''
x = PE["X"]
y = PE["Y"]
z = PE["Z"]
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#plt.show()
'''


PE[PE.duplicated()]
lx = PE[PE.duplicated()]['X'].tolist()
lY = PE[PE.duplicated()]['Y'].tolist()
lz = PE[PE.duplicated()]['Z'].tolist()

yi = []

print (len(lY))

for j in range(len(lx)):
     for i in range(179):
         if lx[j] == PE['X'][i] and lY[j] == PE['Y'][i] and lz[j] == PE['Z'][i]:
             print (lx[j],lY[j],lz[j],i)
             yi.append(i)
         else:
             pass

datax = np.linspace(0,179,180)
datax
datay = [0 for x in range(0, 180)]
    
print (len(datay))
#print (len(datax))

for j in yi:
     datay[j] = 1
#datay


#print(datax)
##print(datay)
#plt.plot(datax, datay, 'b.-')
#plt.show()



