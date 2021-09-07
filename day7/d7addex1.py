x = int(input("How much money do you have: "))
y = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
     18: 'eighteen', 19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
     100: 'hundred', 1000: 'thousand', 1000000: 'million'}
n = []
v = []
p = 10
while x != 0:
     b = x % p
     p *= 10
     x -= b
     if b >= 100:
         n.append(p // 100)
         n.append(b // (p // 100))
     else:
         n.append(b)
n = n[::-1]
if 100000 in n:
     n.insert(n.index(100000), 100)
     n.remove(100000)
if 10000 in n:

     n1 = n[n.index(10000)-1] * 10
     n2 = n[n.index(10000)+1]
     n.pop(n.index(10000)-1)
     n.pop(n.index(10000)+1)
     if n1 < 20:
          n.insert(n.index(10000), n1 + n2)
     else:
          n.insert(n.index(10000), n1)
          n.insert(n.index(10000), n2)
     n.remove(10000)
if sum(n) < 20:
     n1 = sum(n)
     n.clear()
     n.append(n1)
while 0 in n:
     n.remove(0)
for item in n:
     v.append(y[item])

print(*v)
