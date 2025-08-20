# 6. Read three integers and print their maximum.
A = int(input("Enter 1st value"))
B = int(input("Enter 2st value"))
C = int(input("Enter 3st value"))

if A > B and A > C:
    print("A is Greater")
elif B > A and B > C:
    print("B is Greater")
else:
    print("C is Greater")
