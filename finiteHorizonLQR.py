# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import scipy.integrate as it
import numpy as np
j = 1 # scales in x (or time)
def order2(Y,t):
    return [Y[1], -(b*Y[1]+c*(Y[0]))/a]

time = np.arange(0, 15/j, 0.01) 
pos,vel,acc,jerk = it.odeint(order4,[1.0,0.0,0.0,0.0],time).T 
axes[2].plot(time, -vel, color='k')
axes[2].set_title('order 4')
