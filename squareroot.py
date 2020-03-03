#Brendan Ryan Feb 2020
#Find squareroot of float number
#
#



#functions

def mySqrt(x):

    r = x
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r


# workings and output

x = float(input("enter value to be rooted:"))
#print(input("this is a test" (mySqrt(x)))
print(math.sqrt(x))

