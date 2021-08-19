x = int(input("Enter first side of triangle "))
y = int(input("Enter second side of triangle "))
z = int(input("Enter third side of triangle "))
p = (x + y + z) / 2
s = p*(p-x)*(p-y)*(p-z)
print(f"area is={s ** (1/2)} cm")
