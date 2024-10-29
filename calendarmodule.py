#learning calendar and datetime module

import calendar

import datetime

print("any month's calendar",calendar.month(2023,4)) #display calendar for april 2023

#Syntax:  calendar.month(year,month_number)

print("2024 calendar",calendar.calendar(2024)) #display calendar of whole year 2024

#Syntax:  calendar.calendar(year)

year = int(input("enter a year: "))

print("check whether entered year is leap or not True if leap,False if non-leap")

print(calendar.isleap(year)) #check whether year is leap or not

#Syntax    calendar.isleap(year)

print("number of leap year between 2000 and 2024",calendar.leapdays(2000,2024))

#Syntax    calendar.leapdays(year1,year2)

print("current date and time")

print(datetime.datetime.now())  #current date and time

#Syntax:  datetime.datetime.now()



