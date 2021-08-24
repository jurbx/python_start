x = int(input("Day= "))
y = x % 400
z = x % 100
k = x % 100
if y == 0 and z != 0 and y == 0:
    print("Year is leap")
else:
    print("Year is not leap")
