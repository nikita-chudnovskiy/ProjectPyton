"""c = 4782
kol =0
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
    last=x%10 # Если посл цифра без остатка делилась на 2, то переменных кол четных увеличиваем на 1
    kol=kol+1
    if last%2==0:
        kol_ch+=1
    s=s+last
    pr =pr*last
    if last>maxim:
        maxim=last
    if last < minn:
        minn = last
    x = x//10
print('Всего цифр: ', kol)
print('Всего четных: ', kol_ch)
print('Сумма всех цифр: ', s)
print('Произведение всех цифр ', pr)
print('max ', maxim)
print('min ', minn)
