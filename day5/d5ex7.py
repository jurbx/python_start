import random
m = 12
l1 = []
x = 0
for i in range(1, m + 1):
    i1 = random.randint(7500, 12000)
    l1.append(i1)
    x += i1

x /= m
print(l1)
print("Avg num is", x)

