# This program will calculate a persons BMI using figures provided
# user is asked to enter weigth and height

# BMI IS weight divided by height in meters squared
weight = float(input("Enter your weight in KG; "))#user asked for input
height = float(input("Enter your height in meters; "))#user asked for input

heightsquared = (height * height)#calculate the square of height
bmi = weight / heightsquared #defing the variable BMI

#now round to two decimal places
bmi2 = (round (bmi,2))

print("Your BMI is",bmi2,"based on the figures you have provided")