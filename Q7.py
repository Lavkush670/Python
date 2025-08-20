# 7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).

a = int(input("Enter angle 1"))
b = int(input("Enter angle 2"))
c = int(input("Enter angle 3"))

if a + b + c == 180:
    if a == 90 or b == 90 or c == 90:
        print("Right Angle Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Angle Triangle")
    else:
        print("Acute Angle Traingle")
else:
    print("Invalid Triangle")