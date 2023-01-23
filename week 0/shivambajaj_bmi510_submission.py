# -*- coding: utf-8 -*-
"""ShivamBajaj_BMI510_Submission.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FiYTeWXVqeVV69L6Y-zenaZ3euDWaAlx
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""Question 1"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [589.6, 1173.8, 1758, 2344.8, 2930, 3514.7, 4098.8, 4685, 5269, 5854]

def slope(x1, y1, x2, y2):
  return (y2-y1)/(x2-x1)

def intercept(x1, y1, x2, y2):
  slopes = slope(x1, y1, x2, y2)
  y_intercept = -x1*slopes+y1
  return y_intercept

sloper = []
interceptr = []

for i in range(10):
  if i!=9:
    sloper.append(slope(x[i],y[i],x[i+1],y[i+1]))
    interceptr.append(intercept(x[i],y[i],x[i+1],y[i+1]))

print(f'Slope : {np.average(sloper)} \nIntercept: {np.average(interceptr)}')
print(f'The best fit equation is y = {np.average(sloper)}*x + {np.average(interceptr)}')

"""Question 2"""

def MacLaurinCal(x):
  ans = 0

  for n in range(x):
    ans += math.pow(-1,n) / ((2*n)+1)
  return ans*4

print(f'estimated pi = {MacLaurinCal(10)}')

print(f'estimated pi = {MacLaurinCal(100)}')

print(f'estimated pi = {MacLaurinCal(1000)}')

print(f'estimated pi = {MacLaurinCal(10000)}')