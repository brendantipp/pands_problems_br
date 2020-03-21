#task 8 brendan ryan
# march 17th 2020
# Write a program that displays 
# a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes. 

##import librarys required

import numpy as np
import matplotlib.pyplot as plt

##create definitions
def f(x):
    return x

def g(x):
    return x**2

def h(x):
    return x**3

#the range required 
x = np.arange(0,4)

##plotting the results

plt.plot (f(x),g(x),h(x))
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("brendans graph")
plt.show()










