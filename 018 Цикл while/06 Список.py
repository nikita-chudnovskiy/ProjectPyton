# Вывести все цифры в списке больше 100
a = [102,19,2,101,3,5,4,2,6,103]
while len(a)>0:
    cifra=a[0]
    if cifra>100:
        print(a[0],end =' ')
    a=a[1:]

print()

a =[2,3]
i =0
while len(a)>i:
    print(a[i])
    i+=1
