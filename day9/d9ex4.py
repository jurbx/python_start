from random import randint


def search_in_list(research, list1):
    if isinstance(research, list) or isinstance(research, tuple):
        for item1 in research:
            for item in range(len(list1)):
                if list1[item] == item1:
                    print(item1, item, sep=': ')
    else:
        for item in range(len(list1)):
            if list1[item] == research:
                print(research, item, sep=': ')
    return -1


research1 = (1, 2, 4, 12)
list1 = [randint(2, 90) for item in range(200)]
print(search_in_list(research1, list1))
