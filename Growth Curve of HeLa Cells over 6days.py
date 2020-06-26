# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:12:58 2020

@author: meaga
"""


import matplotlib.pyplot as plt 


x =[0, 1, 2, 3, 4, 5, 6,]
y = [0,200000, 600000, 850000, 1500000, 1600000, 1000000]


plt.plot(x, y)
plt.xlabel('Days')
plt.ylabel ('Cell Growth/ml')
plt.title('Growth Curve')
plt.show()