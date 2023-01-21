def lstcode():
    lst = []
    strng=''
    while True:
        value = input('Enter the value:  ')
        if value == '':
            break
        lst = lst + [value]
    for value in lst :
        print (' , '.join(lst[0:-1]) + ', and ' + lst[-1])
        break
lstcode()