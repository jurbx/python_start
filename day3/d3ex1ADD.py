x = int(input("Enter room`s number "))
if 0 < x <= 36:
    print("Room is at first entrance")
    x %= 4
elif x <= 72:
    print("Room is at second entrance")
    x /= 2
    x %= 4
elif x <= 108:
    print("Room is at third entrance")
    x /= 3
    x %= 4
elif x <= 144:
    print("Room is at fourth entrance ")
    x /= 4
    x %= 4

else:
    print("Incorrect number")
if 8 < x <= 9:
    print("Room is at 9 floor")
elif 7 < x <= 8:
    print("Room is at 8 floor")
elif 6 < x <= 7:
    print("Room is at 7 floor")
elif 5 < x <= 6:
    print("Room is at 6 floor")
elif 4 < x <= 5:
    print("Room is at 5 floor")
elif 3 < x <= 4:
    print("Room is at 4 floor")
elif 2 < x < 3:
    print("Room is at 3 floor")
elif 1 < x <= 2:
    print("Room is at 2 floor")
elif 0 < x <= 1:
    print("Room is at 1 floor")
else:
    print("Something goes wrong")