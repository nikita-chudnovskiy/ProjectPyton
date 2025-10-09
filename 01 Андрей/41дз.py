# words = {
#
# }
# while True:
#     d = input('Введите команду: ')
#     if d == 'найти':
#         b = input('Введите слово: ')
#         if b not in words:
#             print('Такого слова в словаре нет.')
#         if b in words:
#             print(words[b])
#     if d == 'добавить':
#         g = input('Введите слово: ')
#         h = input('Введите определение слова: ')
#         words[g] = h
#     if d == 'стоп':
#         break

words = {

}
while True:
    d = input('Введите команду: ')
    if d == 'найти':
        b = input('Введите предложение: ')
        for i in b.split():
            if i in words:
                print(words[i])
    if d == 'добавить':
        g = input('Введите слово: ')
        h = input('Введите определение слова: ')
        words[g] = h
    if d == 'стоп':
        break