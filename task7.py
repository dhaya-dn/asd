import calendar
year=int(input("Enter the year : "))
month=int(input("enter the month : "))
print(calendar.monthrange(year,month)[1])
