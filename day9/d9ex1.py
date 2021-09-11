from random import randint


def max_in_list(list0):
    return max(list0)


list1 = [randint(1, 60) for i in range(15)]
print(*list1, sep=', ')
print(max_in_list(list1))