a = '1ad23,236sdsRTY'
while len(a)>0:
    bukva = a[0]
    if bukva >='a'and bukva<='z':
        print(bukva,'smol')
    elif bukva >='A'and bukva <= 'Z':
        print(bukva,'big')
    elif bukva.isdigit():
        print(bukva,'didgit')
    else:
        print('znak')

    a = a[1:] # заменяем нашу строку на срез всех символов кроме первого
