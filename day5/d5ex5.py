list1 = [0, 5, 2, 4, 7, 1, 3, 19]
s = 0
for i in list1:
    if i % 2:
        print(i)
        s += 1
    else:
        continue
print(s)