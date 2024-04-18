# EulerPlotter
ODE - First Order Euler Method class with Plotting functions

## Sample Usage
`
import numpy as np
import matplotlib.pyplot as plt

f = lambda arr: arr[1]
g = lambda arr: -mu*(arr[0]**2-1)*arr[1]-arr[0]
x0 = 1 # Initial Condition
p0 = 0
# create EulerPlotter
ep = EulerPlotter([f,g],[x0,p0],0.01,30)
ep.getResultArray()
ep.twoDPlot(plt,[0,1],[12,4],"1) x over t")
plt.show()
`
