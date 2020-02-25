#Brendan Ryan
#Return messsage to user based on day being weekday or weekend


import datetime

today = datetime.datetime.now()

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

Weekday = days[0:6]

Weekend = days[6:-1]

for days in Weekday
    print("na its a weekday")

for days in Weekend
    print ("yesss its the weekend")




