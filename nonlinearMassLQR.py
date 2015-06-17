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

R = matrix([[1]]) 
Rinv = R # do inverse in cases where it is needed here
#F = matrix([[2*w1*w1*w1 - Qb,w1*w1],[w1*w1,2*w1]]) # what to put in here...
startTime = 0.1
T = 1 + startTime 
W = 4#np.sqrt(0.5)
#F = matrix([[0,W*W/(T*T)],[W*W/(T*T),2/T]]) # what to put in here...
#F = matrix([[0.25,0.1],[0.1,0.97]]) # what to put in here...
#F = matrix([[0.25*15.2,0.1*8],[0.1*8,0.97*2.5]]) # what to put in here...
F = matrix([[0.25*200,0.1*50],[0.1*50,0.97*5]]) # what to put in here...
#F = matrix([[0.25/16,0.1/10],[0.1/10,0.97/2.8]]) 
#F = matrix([[0.25/8,0.1/10],[0.1/10,0.97/1.8]]) 
#F = matrix([[5260,420],[420,50]]) # what to put in here...

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

for i in range(1,steps):
    w = W/(startTime + (steps-i)/steps)
#    w = W/(startTime + i/steps)
    Q = matrix([[w*w*w*w,0],[0,2*w*w]])
    Ps[i] = Ps[i-1] + backwards(Q, Ps[i-1], 0)*dt
  
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
pa = [0]
pb = [0]
pc = [0]
pd = [0]
#2 forwards pass
for i in range(1,steps):
    x[i] = x[i-1] + forwards(x[i-1], steps-i)*dt
    pos.append(x[i].item(0))
    vel.append(x[i].item(1))
    dif.append(0.1*(vel[i] - vel[i-1])/dt)
#    pa.append(Ps[steps-i].item(0) * np.power(startTime + (steps-i)/steps, 3))
#    pb.append(Ps[steps-i].item(1) * np.power(startTime + (steps-i)/steps, 2))
#    pc.append(Ps[steps-i].item(2) * np.power(startTime + (steps-i)/steps, 2))
#    pd.append(Ps[steps-i].item(3) * np.power(startTime + (steps-i)/steps, 1))
    pa.append(Ps[steps-i].item(0) * np.power(startTime + i/steps, 3))
    pb.append(Ps[steps-i].item(1) * np.power(startTime + i/steps, 2))
    pc.append(Ps[steps-i].item(2) * np.power(startTime + i/steps, 2))
    pd.append(Ps[steps-i].item(3) * np.power(startTime + i/steps, 1))
    spring.append(Ps[steps-i].item(2))
    damping.append(Ps[steps-i].item(3))
    stiffness.append(np.sqrt(Ps[steps-i].item(2)) * (startTime + i/steps))
#    stiffness.append(np.sqrt(Ps[steps-i].item(2)) * (startTime + (steps-i)/steps))
    dampingratio.append(0.5*Ps[steps-i].item(3) / np.sqrt(Ps[steps-i].item(2)))
    blah = Ps[steps-i].item(2)*x[i].item(0) + Ps[steps-i].item(3)*x[i].item(1)


plt.plot(vel)
plt.plot(pos)
#plt.plot(dif)
#plt.figure()
#plt.plot(spring)
#plt.plot(damping)
plt.figure()
plt.plot(pa)
plt.plot(pb)
#plt.plot(pc)
plt.plot(pd)
plt.figure()
plt.plot(stiffness)
plt.plot(dampingratio)

plt.figure()
plt.plot([-2,-1,-0.5,-0.25,0,0.25,0.5,1,1.5,2], [0.8176,0.829,0.861,0.906,1,1.151,1.32,1.63,1.858,2.0105])
plt.figure()
plt.plot([-2,-1,-0.5,-0.25,0,0.25,0.5,1,1.5,2], [-1/2.66,-1/3.03,-1/3.897,-1/5.74,0,1/2.786,1/1.026,1/0.327,1/0.1589,1/0.09366])
plt.figure()
plt.plot([-1/2.66,-1/3.03,-1/3.897,-1/5.74,0,1/2.786,1/1.026,1/0.327,1/0.1589,1/0.09366], [0.8176,0.829,0.861,0.906,1,1.151,1.32,1.63,1.858,2.0105], '.')