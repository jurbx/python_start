def palindrome(list1):
    for item in range(900, 1000):
        for item1 in range(900, 1000):
            number = item * item1
            number1 = str(number)
            if number1 == number1[::-1]:
                list1.append(number1)
    return max(list1)


list2 = []
print(palindrome(list2))