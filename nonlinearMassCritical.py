# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import numpy as np
from numpy import matrix
T = 1 
w0 = 1
w1 = 0.1
zeta = 1

def backwards(x,v,w,i):
    cs[i] = 1+(x/v - (1/w))/2;
    return -w*w*x + 2*cs[i]*w*v;   
def forwards(x, t):
    return 0
    
#1 backwards pass
steps = 10000
dt = 4.0/steps;
xs = [1 for i in range(0,steps)]
vs = [w1 for i in range(0,steps)]
cs = [0 for i in range(0,steps)]
ex = [0 for i in range(0,steps)]
rs = [0 for i in range(0,steps)]

for i in range(steps-2,0,-1):
    acc = backwards(xs[i+1], vs[i+1], w0, i);
    ex[i] = (cs[i+1]-cs[i])/(dt*(cs[i]-1))
    vs[i] = vs[i+1]+acc*dt;
    xs[i] = xs[i+1]+vs[i]*dt;
    rs[i] = xs[i]/vs[i];
    
ex[steps-2] = 0;
  
plt.plot(cs);
plt.plot(xs);
plt.plot(vs);
plt.plot(ex);
plt.plot(rs);
# something is not right, the x/v goes below 1/w0
# the damping ratio c doesn't go below 1.6ish
# but at 1084, x/v is about 1, so why isn't cs[1084] 1?
# it is 2!