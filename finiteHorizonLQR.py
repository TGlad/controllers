# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import scipy.integrate as it
import numpy as np
from numpy import matrix
A = matrix([[0,1],[0,0]])
B = matrix([[0], [1]])
F = matrix([[10,0],[0,10]]) # what to put in here...
Q = matrix([[1,0],[0,2]])
R = matrix([[1]]) 
Rinv = R # do inverse in cases where it is needed here
#Ps = matrix([[1]])

def backwards(P, t):
    # sympy has a matrix class with matrices in
    return A.transpose()*P+P*A  - (P*B)*Rinv*(B.transpose()*P) + Q   
def forwards(x, t):
    K = Rinv*(B.transpose() * Ps[t])
    u = -K*x
    return A*x + B*u
    
#def finiteHorizonLQR(A,B,F,Q,R): # ignoring the N matrix, not usually needed
time = np.arange(0, 1, 0.01) 
#1 backwards pass
Ps = [F for i in range(0,100)]
dt = 0.01;
for i in range(1,100):
    Ps[i] = Ps[i-1] + backwards(Ps[i-1], 0)*dt
x = matrix([[1],[0]])
for i in range(1,100):
    x[i] = x[i-1] + forwards(x[i-1], 100-i)*dt
    
#Ps,t = it.odeint(backwards,F,time).T 
plt.plot(time, x)
#2 forwards pass
#x,t = it.odeint(forwards,[1,0],time).T 
#plt.plot(time, x)


#finiteHorizonLQR(A,B,F,Q,R);