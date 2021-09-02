text = " dawdawdw d  dawd<div id="" style="">d qwdawdaw daw<div id= style="">"
while "<" and ">" in text:
    x = text.find("<")
    y = text.find(">")
    text = text[:x] + text[y+1:]
print(text)