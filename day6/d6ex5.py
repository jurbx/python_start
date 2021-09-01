import string
text = input("text= ")
l = []
for item in string.punctuation:
    text.replace(item, "")
text = text.split()
for i in text:
    x = len(i)
    l.append(x)
print(max(l))
