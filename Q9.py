# 9. WAP to check whether a year is a leap year or not.

year = int(input("Enter year as you wish"))

if year % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")