# r = []
# for i in range(10):
#     b = int(input())
#     r.append(b)
# print('Максимальное число:',max(r))

# b = 0
# print('Введите текст: ')
# d = input()
# for i in d.split():
#     if len(i) >3:
#         b = b+1
# print('Количество слов длиннее 3 букв:',b)

import requests
t = input()
d = requests.get('https://restcountries.com/v3.1/name/'+t)
if d.status_code == 200:
    g = d.json()
    print(g[0]['population'])