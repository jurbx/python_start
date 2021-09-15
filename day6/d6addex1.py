text = "catcatcatcataaaaaititit"
l = []
n = 0
while text != "":
    for number in range(1, len(text)):
        if text[:number] == text[number: number + number]:
            l.append(text[:number])
            if l[n].isalpha():
                text = text.replace(l[n], "")
                n += 1
                break

print(min(l))