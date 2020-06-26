# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:58:29 2020

@author: meaga
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,t,k):
    dydt = k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODEs
k = 0.6
y1 = odeint(model,y0,t,args=(k,))
k = 0.7
y2 = odeint(model,y0,t,args=(k,))
k = 0.5
y3 = odeint(model,y0,t,args=(k,))

# plot data
td =[0, 1, 2, 3, 4, 5, 6,]
yd= [0,200000, 600000, 850000, 1500000, 1600000, 1000000]
plt.plot(td, yd, 'rd')


# plot results
plt.plot(t,y1,'r-',linewidth=2,label='k=0.6')
plt.plot(t,y2,'b--',linewidth=2,label='k=0.7')
plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()