a ='privet'
while len(a)>0:
    print(a[0],a[1:])
    a=a[1:] # заменяем нашу строку на срез всех символов кроме первого

# Обход строки
a = '1aR#'
while len(a)>0:
    bukva = a[0]
    if bukva >='a'and bukva<='z':
        print(bukva,'smol',end=' ')
    elif bukva >='A'and bukva <= 'Z':
        print(bukva,'big',end=' ')
    elif bukva.isdigit():
        print(bukva,'didgit',end=' ')
    else:
        print(bukva,'znak')
    a = a[1:] # заменяем нашу строку на срез всех символов кроме первого

# Обход списка
a = ['Привет', 99, 88, 77, 66, 55]
while len(a) > 0:
    print(a[0],end=' ')
    a = a[1:] # заменяем нашу строку на срез всех символов кроме первого
print()
# 2 Вариант
a = [1,2,3,'Привет']
i = 0
while i<len(a):
    print(a[i],end=' ')
    i=i+1
