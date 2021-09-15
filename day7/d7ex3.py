x = {}
y = input("Word= ")
x1 = 1
for item in y:
    if x.get(item):
        continue
    else:
        x[item] = y.count(item)
print(x)
