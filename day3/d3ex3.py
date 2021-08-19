import math.abs
x, y = float(input("x = ")), float(input("y = "))
if y >= abs(x) and y <= 1.0:
    print(True)
else:
    print(False)
