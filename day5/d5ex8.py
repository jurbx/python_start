l1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
x = 0
for item in l1:
    print(*item, sep=", ")
    x += sum(item)
print(x)