# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:12:42 2020

@author: meaga
"""


import numpy as np
from math import log
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(ym,t):
#    a = 0.9
    b = 100000
   
    if t <=3: 
       a = 0.45
    else:
       a =-0.4
       
    dydt = log(2)/a *ym*(1-ym/b)
    return dydt

# initial condition
y0 = 10000


# time points
t = np.linspace(0,5)

# solve ODE
ym = odeint(model,y0,t)

# plot data
td =[0, 1, 2, 3, 4, 5, 6,]
yd= [0,200000, 600000, 850000, 1500000, 1600000, 1000000]
plt.plot(td,yd,'*')

# plot results
plt.plot(t,ym)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()