# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
#import scipy.integrate as it
from numpy import matrix
A = matrix([[0,1],[0,0]])
B = matrix([[0], [1]])
dt = 0.05
# this is for catch (pos, vel, time constraints)
#F = matrix([[12/(dt*dt*dt),6/(dt*dt)],[6/(dt*dt),4/dt]]) # what to put in here...
# this is for intercept (pos, time contraints, and low accel)
F = matrix([[3/(dt*dt*dt),3/(dt*dt)],[3/(dt*dt),3/dt]]) # what to put in here...
Q = matrix([[0,0],[0,0]])
R = matrix([[1]]) 
Rinv = R # do inverse in cases where it is needed here
#Ps = matrix([[1]])

def backwards(P, t):
    # sympy has a matrix class with matrix inverses in
    diff = A.transpose()*P+P*A
    diff2 =  -(P*B)*Rinv*(B.transpose()*P) + Q
    return diff + diff2   
def forwards(x, t):
    K = Rinv*(B.transpose() * Ps[t])
    u = -K*x
    return A*x + B*u
    
#def finiteHorizonLQR(A,B,F,Q,R): # ignoring the N matrix, not usually needed
#1 backwards pass
steps = 10000
Ps = [F for i in range(0,steps)]
dt = 1.5/steps;
for i in range(1,steps):
    Ps[i] = Ps[i-1] + backwards(Ps[i-1], 0)*dt
x = [matrix([[1],[0]]) for i in range(0,steps)]
pos = [1]
vel = [0]
dif = [0]
spring = [0]
damping = [0]
other = [0]
#2 forwards pass
for i in range(1,steps):
    x[i] = x[i-1] + forwards(x[i-1], steps-i)*dt
    pos.append(x[i].item(0))
    vel.append(x[i].item(1))
    dif.append(0.4*(vel[i] - vel[i-1])/dt)
    spring.append(Ps[steps-i].item(2))
    damping.append(Ps[steps-i].item(3))
    blah = Ps[steps-i].item(2)*x[i].item(0) + Ps[steps-i].item(3)*x[i].item(1)

    
plt.plot(vel)
plt.plot(pos)
plt.plot(dif)
plt.figure()
plt.plot(spring)
plt.plot(damping)