# 12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. 
# You have to tell whether the triangle is valid or not. 
# A triangle is valid if the sum of its angles equals 180.

angle1 = int(input("Enter angle 1\n"))
angle2 = int(input("Enter angle 2\n"))
angle3 = int(input("Enter angle 3\n"))

if angle1 + angle2 + angle3 == 180:
    print("This is a valid triangle")
else:
    print("This is not a valid triangle")

