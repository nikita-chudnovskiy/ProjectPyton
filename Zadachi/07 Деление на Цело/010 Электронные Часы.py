# Элетронные часы вводим 150 мин
n=int(input('введите кол-во минут:'))
print('Прошло',n // 60 % 24  ,'часов', n % 60 ,'минут')

# Количество парт понадобится 3 классам
a,b,c = map(int,input().split())
print((a+b+c)//2+(a+b+c)%2)