#Break
print("введите чтонибудь")

while True:
    s = input()
    if s == 'Выход':
        break

print('длина строки', len(s))

# Continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'Выход':
        break
    if len(s) < 5:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')
# Разные другие действия здесь...