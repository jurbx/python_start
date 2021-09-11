from string import punctuation


def first_sub(list1):
    list1.append(list1[len(list1)-1] + list1[1] - list1[0])
    return list1


def second_sub(list1):
    list1.append(list1[len(list1)-1] * list1[1] // list1[0])
    return list1


def third_sub(list1):
    list1.append(int(list1[len(list1)-1] ** 0.5 + list1[1] ** 0.5 - list1[0] ** 0.5) ** 2)
    return list1


def fourth_sub(list1):
    list1.append(int(list1[len(list1) - 1] ** (1/3) + list1[1] ** (1/3) - list1[0] ** (1/3)) ** 3)
    return list1


numbers = input('Enter numbers(3 min)= ')
for item in punctuation:
    if item == '.':
        continue
    numbers = numbers.replace(item, ' ', numbers.count(item))
numbers = numbers.split()
numbers = [int(item) for item in numbers]

if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
    print(*first_sub(numbers), sep=', ')
elif numbers[1] // numbers[0] == numbers[2] // numbers[1]:
    print(*second_sub(numbers), sep=', ')
elif int(numbers[1] ** 0.5 - numbers[0] ** 0.5 == numbers[2] ** 0.5 - numbers[1] ** 0.5):
    print(*third_sub(numbers), sep=', ')
elif int(numbers[1] ** (1/3) - numbers[0] ** (1/3) == numbers[2] ** (1/3) - numbers[1] ** (1/3)):
    print(*fourth_sub(numbers), sep=', ')
else:
    print('Incorrect subsequence')
