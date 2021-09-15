x = int(input("num= "))
y = 2
while y < x and x >= 1:
    if x % y == 0:
        print(False)
        break
    y += 1
else:
    print(True)