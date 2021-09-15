n = int(input("num= "))
j = 0
for i in range(n, 0, -2):
    print(" " * j, "*" * i, sep="")
    j += 1
j -= 2
for i in range(3, n + 1, 2):
    print(" " * j, "*" * i, sep="")
    j -= 1