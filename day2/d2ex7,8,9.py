x = int(input("Enter number "))
y = 0
k = x
b = x
while x > 0:
    z = x % 10
    x = x // 10
    y += z
    print(z)
print("sum is ", y)
print("len is", len(str(k)))


