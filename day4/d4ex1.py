y = []
x = int(input("Enter number "))
n = x
while n > 0:
    x = n % 10
    y.append(x)
    n //= 10
y.reverse()
k = len(y) // 2
half1 = sum(y[:int(k)])
half2 = sum(y[int(k):])
if half1 == half2:
    print("Ticket is lucky")
else:
    print("Ticket is not lucky")