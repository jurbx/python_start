list1, list2 = [], []
[list1.append(i) for i in range(1, 101) if not i % 3]
[list2.append(i) for i in range(1, 101) if not i % 5]
list1, list2 = set(list1), set(list2)
list3 = list1 & list2
print(list3)