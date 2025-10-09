# import requests
# f = requests.get('https://fakestoreapi.com/products')
# if f.status_code == 200:
#     g = f.json()
#     for i in g:
#         print(i['title'])
#         print(i['price'])

import requests
s = input()
w = requests.get('https://ru.wikipedia.org/api/rest_v1/page/summary/'+s)
if w.status_code == 200:
    d = w.json()
    print(d['extract'])
if w.status_code != 200:
    print('Ошибка')
