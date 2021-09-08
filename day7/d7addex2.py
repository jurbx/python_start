romennumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}  # Программа работает до 388

inputnumbers = input('Num= ')

inputnumbers = inputnumbers.upper()     # Переводит все буквы в верхний регистр

numbers = []

check = ['V', 'X', 'C', 'L']
case = 0

for item in inputnumbers:
    numbers.append(item)    # Добавляет все элементы строки по отдельности

for item in check:
    while item in numbers and numbers.index(item) > 1 and numbers[numbers.index(item)-1] == numbers[numbers.index(item)-2] == 'I':
        numbers.pop(numbers.index(item)-1)   # Удаляет лишние I которые стоят до item (максимум 1), если item есть в строке

    while item in numbers and numbers.index(item) <= len(numbers)-5 and numbers[numbers.index(item)+1] == numbers[numbers.index(item)+4] == 'I':
        numbers.pop(numbers.index(item)+1)   # Удаляет лишние I которые стоят после item (максимум 3), если item есть в строке

    while numbers.count(item) > 3:
        numbers.remove(item)     # Удаляет лишние item, если в списке других цифр нету (макс 3)

    while 'V' in numbers and numbers.count('V') > 1:
        numbers.remove('V')     # Удаляет лишние V (макс 1)

print(*numbers)     # Выводит все римские цифры, которые будут расшифрованы

check1 = check[:check.index('C')]
check2 = check[check.index('C'):]

for item in numbers:
    case += romennumber[item]
    for item1 in check1:
        if numbers.index(item) != len(numbers)-1 and item == 'I' and numbers[numbers.index(item)+1] == item1:
            case -= 2   # Если перед item1['V', 'X'] стоит I, вычитает из item1 единицу
    for item2 in check2:
        if numbers.index(item) != len(numbers)-1 and item == 'X' and numbers[numbers.index(item)+1] == item2:
            case -= 20  # Если перед item2['C', 'L'] стоит X, вычитает из item2 10

        else:
            continue

print(case)