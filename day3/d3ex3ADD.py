x = int(input("Enter first side of triangle "))
y = int(input("Enter second side of triangle "))
z = int(input("Enter third side of triangle "))
if (x + y) > z and (x + z) > y and (z + y) > x:
    print("Triangle can exist")
else:
    print("Triangle cannot exist")