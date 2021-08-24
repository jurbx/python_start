x = int(input("Enter number 1 "))
y = int(input("Enter number 2 "))
z = int(input("Enter number 3 "))
if x > y and x > z:
    print("First number is the largest")
elif y > z:
    print("Second number is the largest")
else:
    print("Third number is the largest")