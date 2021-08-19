x = int(input("Enter 16 digit credit card number "))
y = x // 1000 % 10
z = x // 100 % 10
c = x // 10 % 10
v = x % 10
print(y, z, c, v, sep="\n")