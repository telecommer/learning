from os import system, name
import datetime


y = "2022-01-01 00:00:02.000000"
z = "2022-01-01 00:00:00.000000"
x = str(datetime.datetime.now())
while x < y:
    x = str(datetime.datetime.now())
    system('clear')
    if x > z:
        print("Happy New Year! 2022")
        break
    else:
        print(x +" Fuck 2021")