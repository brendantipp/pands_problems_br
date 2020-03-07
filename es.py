## Brendan Ryan - Task 7
## March 2020
## Description - Program that reads in a text file as inputted and retruns the count of the characters 
# The user is requested to input the filename and character they wish to find 
#

#ask user to input the file name
filename = (input("Enter the file name:"))

#ask user to input the character they wish to find
character = (input("Enter character you wish to find:"))

#Open file as read and define as result

with open(filename, 'r') as file:

    result= file.read()

#output the result

print("There is:",result.count(character),"",character,"s in that file")






    





       
