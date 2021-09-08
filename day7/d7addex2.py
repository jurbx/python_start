romennumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

inputnumbers = input('Num= ')

inputnumbers = inputnumbers.upper()     # Переводит все буквы в верхний регистр

numbers = []

case = 0

for item in inputnumbers:
    numbers.append(item)    # Добавляет все элементы строки по отдельности

while 'V' in numbers and numbers.index('V') > 1 and numbers[numbers.index('V')-1] == numbers[numbers.index('V')-2] == 'I':
    numbers.pop(numbers.index('V')-1)   # Удаляет лишние I которые стоят до V (максимум 1), если V есть в строке

while 'V' in numbers and numbers.index('V') <= len(numbers)-5 and numbers[numbers.index('V')+1] == numbers[numbers.index('V')+4] == 'I':
    numbers.pop(numbers.index('V')+1)   # Удаляет лишние I которые стоят после V (максимум 3), если V есть в строке

while numbers.count('I') == len(numbers) and numbers.count('I') > 3:    # Удаляет лишние I, если в списке других цифр нету (макс 3)
    numbers.remove('I')

print(*numbers)     # Выводит все римские цифры, которые будут расшифрованы

for item in numbers:
    case += romennumber[item]
    if numbers.index(item) != len(numbers)-1 and item == 'I' and numbers[numbers.index(item)+1] == 'V':
        case -= 2   # Если перед V стоит I, вычитает из V единицу

    elif numbers.index(item) != len(numbers)-1 and item == 'I' and numbers[numbers.index(item)+1] == 'X':
        case -= 2   # Если перед X стоит I, вычитает из X единицу

    elif numbers.index(item) != len(numbers)-1 and item == 'X' and numbers[numbers.index(item)+1] == 'L':
        case -= 20  # Если перед L стоит X, вычитает из L 10

    else:
        continue

print(case)
