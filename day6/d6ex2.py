name = input("name= ")
while name.isalpha() or name.startswith(name[0].lower()):
    name = input("Enter correct name ")
else:
    print("Things are good")
