"""c = 4782
 while c>0:
    print(c%10)
    kol = kol+1
    c = c//10
print('Всего цифр: ', kol)"""

x =int(input())
kol=0
kol_ch=0
s=0
pr =1
maxim =0
minn = 9
while x>0:
    last=x%10           # last =  последняя цифра числа x
    kol=kol+1
    if last%2==0:
        kol_ch+=1
    s=s+last
    pr =pr*last
    if last>maxim:
        maxim=last
    if last < minn:
        minn = last
    x = x//10           # убираем последнюю цифру
print('Всего цифр: ', kol)
print('Всего четных: ', kol_ch)
print('Сумма всех цифр: ', s)
print('Произведение всех цифр ', pr)
print('max ', maxim)
print('min ', minn)

# обход цифр числа в двоичной системе
x = int(input())
while x > 0:
    last = x % 2
    print(last)
    x = x // 2  # убираем последнюю цифру

