s = 'hello world'
print(len(s))
print(s.count('l'),'вхождения')
print(s.find('l'))# Находим под каким индекс перв вхождение
print(s.find('l',3,6)) # начинаем искать с 3 индекса

s = 'coffe'
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') +1))
print('ХА')