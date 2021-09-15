h = int(input("high= "))
w = int(input("width= "))
print("*"*w)
for i in range(1, h-1):
    print("*", " " * (w-2), "*", sep="")
print("*" * w)