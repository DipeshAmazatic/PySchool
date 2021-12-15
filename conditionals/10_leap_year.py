"""Write a function that determines if a given year is a leap year.
A leap year is divisible by 4, but not by 100, unless it is also divisible by 400."""

def LeapYear(year):
    if(((year % 4 == 0) and (year % 100!= 0)) or (year%400 == 0)):
        return True
    return False
print(LeapYear(2012))
print(LeapYear(2010))