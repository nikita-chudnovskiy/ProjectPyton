s = 'https://pygen.ru/'
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

s = 'zzz'
if '.' not in s:
    print('Введенная строка не содержит символа точки')


if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')

if len(s) == 1 and s in 'aeiou':
    print('YES')