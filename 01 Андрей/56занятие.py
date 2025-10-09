# def tropinka(text):
#     b = 0
#     for i in text:
#         if i == 'а':
#             b = b+1
#     return(b)
#
# f = tropinka('я зашел в ресторан покушать')
# print(f)


# import requests
# t = input()
# w = {
#     'q':t,
#     'appid':'9a00262c5c484d5b7ce58fed75426599',
#     'units':'metric',
#     'lang':'ru'
# }
# a = requests.get('http://api.openweathermap.org/data/2.5/weather',w)
# if a.status_code == 200:
#     e = a.json()
#     print('Температура:',e['main']['temp'])
#     print('Ощущается температура на:',e['main']['feels_like'])
#     print('Описание:',e['weather'][0]['description'])
#     print('скорость ветра:',e['wind']['speed'])

# g = []
# while True:
#     f = int(input())
#     if f != 0:
#         g.append(f)
#     if f == 0:
#         break
# print(g)

import requests
d = requests.get('https://randomuser.me/api/')
if d.status_code == 200:
    q = d.json()
    print(q['results'][0]['name']['title'],q['results'][0]['name']['first'],q['results'][0]['name']['last'])