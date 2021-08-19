apple, orange = 25, 35
x = int(input("money = "))
if x >= orange+apple:
    print("You can buy an apple and orange")
elif x >= orange:
    print("You can buy an orange or apple")
elif x >= apple:
    print("You can  an apple")
else:
    print("You can`t buy anything of fruit")