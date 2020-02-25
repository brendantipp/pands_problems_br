#Brendan Ryan
#Return messsage to user based on day being weekday or weekend


import datetime

today = datetime.datetime.now()

day = today.weekday()
dayname ={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

print("Today is ... ", dayname[day])

#print(days)

if day < 4:
    print("boo its a weekday")
else:
    print("yes its the weekend")






