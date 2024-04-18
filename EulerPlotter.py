import numpy as np
import math as math
import matplotlib.pyplot as plt
import random

class EulerPlotter:
  perturb = 0
  labels = ['t','x','y','z']
  resultArray = []

  # functions is an array of functions [f(array []): return result, ...]
    # representing first derivative of variables
  # initialValues is an array of numbers (in the order of functions)
  # interval and length are numbers

  def __init__(self,functions, initialValues, interval, length):
    self.functions = functions
    self.initialValues = initialValues
    self.interval = interval
    self.length = length

  # perturbation as a floating number
  def setPerturb(self,perturb):
    self.perturb = perturb

  # Return np array of different varaibles, each as an np array
  def getResultArray(self,tStart=0):
    if(len(self.resultArray)>0):
      return self.resultArray
    t = np.arange(0, self.length + self.interval, self.interval) # Numerical grid
    vars = self.functions
    # Explicit Euler Method
    arr = np.zeros((len(vars)+1,len(t)))
    arr[0] = t
    for i in range(1,len(arr)):
      arr[i][0] = self.initialValues[i-1]
    for i in range(0, len(t) - 1):
      input = []
      for k in range(1,len(arr)):
        input.append(arr[k][i])
      for j in range(1,len(arr)):
        arr[j][i+1] = arr[j][i] + self.interval * vars[j-1](input) + self.perturb
    if(tStart>0):
      length = len(arr[0])
      newArr = np.zeros((len(arr),length-int(tStart/self.interval)))
      for j in range(0,len(arr)):
        newArr[j] = arr[j][int(tStart/self.interval):]
      arr=newArr
    self.resultArray = arr
    return arr
  
  def twoDPlot(self, plt, plots, size = [8,6], title = "", customLabel = False, toContinue = False):
    if(toContinue==False):
      plt.figure(figsize = (size[0], size[1])) 
    first = self.resultArray[plots[0]]
    second = self.resultArray[plots[1]]
    l = labels[plots[1]]+' over '+labels[plots[0]]
    if(customLabel != False):
      l = customLabel
    plt.plot(first, second, label=l)
    plt.xlabel(labels[plots[0]])
    plt.title(title)
    plt.legend(loc='lower right')
    return plt
  
  def threeDPlot(self, plt, fig, ax, size = [8,6], title = "", label="System",toContinue = False):
    arr = self.resultArray
    if(self.perturb>0.00000001):
      label += " with Perturb"
    ax.plot3D(arr[1],arr[2],arr[3],label=label)
    plt.xlabel('x')
    plt.ylabel('y')
    ax.set_zlabel('z')
    plt.title(title)
    plt.legend(loc='lower right')
    return plt
