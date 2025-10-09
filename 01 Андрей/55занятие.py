import requests
print('Введите валюту: ')
a = input()
print('Введите количество валюты: ')
d = int(input())
print('Введите валюту на которую нужно перевести курс: ')
g = input()
e = requests.get('https://api.exchangerate-api.com/v4/latest/'+a)
if e.status_code == 200:
    s = e.json()
    x = (s['rates'])
    if g in x:
        print(x[g]*d)
    else:
        print('Такой валюты нет')