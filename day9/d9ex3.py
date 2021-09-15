def rectangle(width, hight):
    print(width * '*')
    for item in range(1, hight-1):
        print('*', ' ' * (width - 4), '*')
    print(width * '*')


width = int(input('Enter rectangle`s width= '))
height = int(input('Enter rectangle`s height= '))
rectangle(width, height)