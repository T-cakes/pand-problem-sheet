#This program gets day of the week and reports whether it is a weekend or weekday

#author: Stephen Caulfield

#credit: https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime
import datetime
#gets current time and date
now = datetime.datetime.now()

#converts date to current day
day = now.strftime("%A")

#checks if the day is either the weekend; if not, then its a weekday
if day == "Friday" or day == "Saturday" or day == "Sunday":
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")