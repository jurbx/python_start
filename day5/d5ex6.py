l1 = [1, 4, 7, 2]
l2 = []
for i in l1:
    i *= 2
    l2.append(i)
l1.extend(l2)
print(l1)


l1 = [1, 4, 7, 2]
l2 = l1 + [item * 2 for item in l1 ]
print(l2)
