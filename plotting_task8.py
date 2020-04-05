#task 8 brendan ryan  -  march 17th 2020
# Write a program that displays 
# a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. 

# Any references research links used :
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-

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

#the range required - up in increments of 1
x = np.linspace(0,4,10)

##plotting the results passing each item in the list above into the fucnctions f g and h
plt.plot (f(x),g(x),h(x))
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("brendans graph")
plt.show()

#testing only to see output of range
#print (f(x),g(x),h(x))