days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thirsday", 5: "Friday", 6: "Saturday"}
x = int(input("Day of month= "))
x %= 7
print(days[x])
