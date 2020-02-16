# Brendan Ryan
#


a = int(input("please enter a positive integer: "))

while a < 1:
    break


#prints value of (a) - if <1 will stop here and print value
#print (a)


while a > 1:

    if a % 2 == 0:
        a =  int(a/2)
        #print (a) for testing
        else:
            a = int((a*3)+1)

        print (a)











