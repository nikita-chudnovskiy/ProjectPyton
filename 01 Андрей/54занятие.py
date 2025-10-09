# a = {
#     'Андрей':11,
#     'Денис':10,
# }
# print(a['Денис'])
# for r in a:
#     print(r)

# import lib54
# lib54.robot(a)

import requests
# a = input('Введите текст: ')
# d = {
#     'client':'gtx',
#     'sl':'ru',
#     'tl':'en',
#     'dt':'t',
#     'q':a
# }
# h = requests.get('https://translate.googleapis.com/translate_a/single',d)
# if h.status_code == 200:
#     k = h.json()
#     print(k[0][0][0])
# if h.status_code != 200:
#     print('Ошибка!!!')

s = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
if s.status_code == 200:
    x = s.json()
    print(x['rates'][('EUR')])