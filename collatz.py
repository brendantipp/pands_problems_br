# Brendan Ryan
#progam that asks user to input a positive integer and outputs the following calculation
#at each step calculate the next value by taking the current value and if it is even
#divide by two if it is odd multiply by three and add one
#have the program end if the current value is one


#ask user to enter a positive value
a = int(input("please enter a positive integer: "))

#if value entered is negative print "not a positive number" and stop
while a < 0:
    print (a,"is not a positive number")
    break


#prints value of (a) when positive integer
while a > 0:
    print (a)
    break

#perform calculations until reaches 1

while a > 1:

    if a % 2 == 0:
        a =  int(a/2)
        
    else:
        a = int((a*3)+1)

    print (a)











