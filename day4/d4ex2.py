x = int(input("Enter number "))
n = x
l0 = []
l1 = []
l2 = []
while n > 0:
    x = n % 10
    l0.append(x)
    n //= 10
l1 = l0[:int(len(l0) // 2)]
l2 = l0[int(len(l0) // 2):]
l2.reverse()
if l1 == l2:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
