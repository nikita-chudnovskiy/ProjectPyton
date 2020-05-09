a ='privet' # Обход списка тоже самое
while len(a)>0:
    print(a[0],a[1:])
    a=a[1:] # заменяем нашу строку на срез всех символов кроме первого

# Обход строки
a = '1abcR#$'
while len(a)>0:
    bukva = a[0]
    if bukva >='a'and bukva<='z':
        print(bukva,'smol')
    elif bukva >='A'and bukva <= 'Z':
        print(bukva,'big')
    elif bukva.isdigit():
        print(bukva,'didgit')
    else:
        print(bukva,'znak')
    a = a[1:] # заменяем нашу строку на срез всех символов кроме первого


