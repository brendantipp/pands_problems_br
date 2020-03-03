#Brendan Ryan Feb 2020
#Find squareroot of float number


# import the buildt in python fucntion match

import math

#functions

def mySqrt(x):

    r = x
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r


# workings and output

#Result using the built function above
x = float(input("enter value to be rooted:"))
print("Result 1 using the built function",mySqrt(x))

#Print result of the built in python function
print("and result using built in function math.sqrt:",math.sqrt(x))
