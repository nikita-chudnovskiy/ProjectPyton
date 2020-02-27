# Обход строки
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

# Обход списка
a = ['Привет', 2, 3, 3, 4, 45, 23, 234, 13]
while len(a) > 0:
    print(a[0])
    a = a[1:]
# 2 Вариант
a = [1,2,3,'Привет']
i = 0
while i<len(a):
    print(a[i])
    i=i+1
