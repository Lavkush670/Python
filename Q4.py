# 4. WAP to check if the number is divisible by 7 or if the last digit is 5.
num = int(input("Enter any number"))

if num % 7 == 0:
    print("the number is divisible by 7")
elif num % 10 == 5:
    print("the last digit is 5")
else:
    print("No one condition true")