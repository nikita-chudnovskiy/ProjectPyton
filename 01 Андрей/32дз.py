# a = input()
# print('Последняя буква:',a[-1])

print('Введите слово:')
a = input()
if a[-1] == 'ь':
    print(a[-2])
else:
    print(a[-1])
