# 15. Accept the percentage from the user and display the grade according to the following criteria.
# Below 25 – D
# 25 to 45 – C
# 45 to 65 – B
# 65 to 85 – A
# Above 85 – A+

marks = int(input("Enter marks"))

if marks >= 85:
    print("A+")
elif marks < 85 and marks >= 65:
    print("A")
elif marks < 65 and marks >= 45:
    print("B")
elif marks < 45 and marks >= 25:
    print("C")
else:
    print("D")