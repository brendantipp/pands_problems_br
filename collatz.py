# Brendan Ryan


a = int(input("enter an integer: "))

#prints value of a - if <1 will stop here and print value
print (a)

#continues if value of a is greater than 1

while a > 1:

    if a % 2 == 0:
       a =  int(a/2)
       #print (a) for testing
    else:
        a = int((a*3)+1)

    print (a)














