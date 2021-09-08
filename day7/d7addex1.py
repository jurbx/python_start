money = int(input("How much money do you have: "))
y = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
     18: 'eighteen', 19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'
     , 1000: 'thousand', 1000000: 'million'}
numbers = []
numfromdict = []
div = 10
while money * 10 >= div:       # Выводит все числа в список по разрядам: 700 -> [7, 100]; 1000 -> [1, 1000]
     b = money % div
     div *= 10
     money -= b

     if b > 100:
         numbers.append(div // 100)
         numbers.append(b // (div // 100))

     else:
         numbers.append(b)

numbers = numbers[::-1]

if 100000 in numbers:     # Если в списке есть 100000, переводит его в 100: [100000] -> [100, 1000]
     numbers.insert(numbers.index(100000), 100)
     numbers.remove(100000)

if 10000 in numbers:      # Если в списке есть 10000, переводит его в 10: [10000] -> [10, 1000]
     n1 = numbers.pop(numbers.index(10000) - 1) * 10
     n2 = numbers.pop(numbers.index(10000) + 1)

     if n1 < 20:    # Если десятки тысяч меньше 20, суммирует их: [10, 5, 1000] -> [15, 1000]
          numbers.insert(numbers.index(10000), n1 + n2)

     else:     # Иначе, пишет их раздельно: [50, 7, 1000] -> [50, 7, 1000]
          numbers.insert(numbers.index(10000), n1)
          numbers.insert(numbers.index(10000), n2)
     numbers.remove(10000)

for item in numbers:      # Выводит числа словами через ключи словаря
     numfromdict.append(y[item])

print(*numfromdict)

