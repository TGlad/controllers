# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
#import scipy.integrate as it
import numpy as np
from numpy import matrix
A = matrix([[0,1],[0,0]])
B = matrix([[0], [1]])
dt = 0.05
# this is for catch (pos, vel, time constraints)
#F = matrix([[12/(dt*dt*dt),6/(dt*dt)],[6/(dt*dt),4/dt]]) # what to put in here...
# this is for intercept (pos, time contraints, and low accel)
# F = matrix([[3/(dt*dt*dt),3/(dt*dt)],[3/(dt*dt),3/dt]]) # what to put in here...
w0 = 5 # a drop in stiffness
qb = 0
Qb = qb*w0*w0*w0
Q0 = matrix([[w0*w0*w0*w0,Qb],[Qb,2*w0*w0]])
w1 = 1
Qb = qb*w1*w1*w1
Q1 = matrix([[w1*w1*w1*w1,Qb],[Qb,2*w1*w1]])
R = matrix([[1]]) 
Rinv = R # do inverse in cases where it is needed here
F = matrix([[2*w1*w1*w1 - Qb,w1*w1],[w1*w1,2*w1]]) # what to put in here...

def backwards(Q,P, t):
    # sympy has a matrix class with matrix inverses in
    diff = A.transpose()*P+P*A
    diff2 = -(P*B)*Rinv*(B.transpose()*P) + Q
    return diff + diff2   
def forwards(x, t):
    K = Rinv*(B.transpose() * Ps[t])
    u = -K*x
    return A*x + B*u
    
#def finiteHorizonLQR(A,B,F,Q,R): # ignoring the N matrix, not usually needed
#1 backwards pass
steps = 10000
halfsteps = 5000
Ps = [F for i in range(0,steps)]
dt = 1.0/steps;

for i in range(1,halfsteps):
    Ps[i] = Ps[i-1] + backwards(Q1, Ps[i-1], 0)*dt
for i in range(halfsteps,steps):
    Ps[i] = Ps[i-1] + backwards(Q0, Ps[i-1], 0)*dt

  
print(Ps[steps-1])
print(Ps[steps//2])
print(Ps[steps//4])
x = [matrix([[1],[0]]) for i in range(0,steps)]
pos = [1]
vel = [0]
dif = [0]
spring = [0]
damping = [0]
stiffness = [0]
dampingratio = [0];
other = [0]
#2 forwards pass
for i in range(1,steps):
    x[i] = x[i-1] + forwards(x[i-1], steps-i)*dt
    pos.append(x[i].item(0))
    vel.append(x[i].item(1))
    dif.append(0.1*(vel[i] - vel[i-1])/dt)
    spring.append(Ps[steps-i].item(2))
    damping.append(Ps[steps-i].item(3))
    stiffness.append(np.sqrt(Ps[steps-i].item(2)))
    dampingratio.append(0.5*Ps[steps-i].item(3) / np.sqrt(Ps[steps-i].item(2)))
    blah = Ps[steps-i].item(2)*x[i].item(0) + Ps[steps-i].item(3)*x[i].item(1)


plt.plot(vel)
plt.plot(pos)
#plt.plot(dif)
#plt.figure()
#plt.plot(spring)
#plt.plot(damping)
plt.figure()
plt.plot(stiffness)
plt.plot(dampingratio)