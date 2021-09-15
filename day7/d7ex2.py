cat = {'petname': 'Barsik',
       'type': 'Simple street cat',
       'age': 9,
       'hobbies': 'Playing with toy mouse'
       }
x = [cat.get(item) for item in cat]
print(' '.join(x))