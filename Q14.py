# 14. Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C.
A = int(input("Enter 1st number"))
B = int(input("Enter 2nd number"))
C = int(input("Enter 3rd number"))

if A < B and A < C:
    print("A is Lesser")
elif B < A and B < C:
    print("B is lesser")
else:
    print("C is lesser")