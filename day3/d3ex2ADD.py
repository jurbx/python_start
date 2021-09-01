x = int(input("Day= "))

if x % 4 == 0 or x % 400 == 0 and x % 100 != 0:
    print("Year is leap")
else:
    print("Year is not leap")
