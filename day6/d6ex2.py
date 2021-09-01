name = input("name= ")
while name.isdigit() or name.startswith(name[0].lower()):
    name = input("Enter correct name ")
else:
    print("Things are good")