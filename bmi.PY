# This program will calculate a persons BMI using figures provided
#enter weigth
#enter height
#

# BMI IS weight divided by height in meters squared

weight = float(input("Enter your weight in KG; "))
height = float(input("Enter your height in meters; "))

heightsquared = (height * height)
bmi = weight / heightsquared

#now round to two decimal places

bmi2 = (round (bmi,2))

print("Your BMI is",bmi2,"based on the figures you have provided")





