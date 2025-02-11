# a = {
#     'Андрей':'Чёрный',
#     'Саша':'Зелёный',
#     'Давид':'Красный',
#     'Ваня':'Синий'
#
# }
# b = input()
# if b in a:
#     print(a[b])
# if b not in a:
#     print('Такого человека нет')

# contacts = {
#
# }
# while True:
#     d = input('Введите команду: ')
#     if d == 'добавить':
#         name = input('Введите имя контакта: ')
#         number = input('Введите номер телефона: ')
#         contacts[name] = number
#         print('Контакт успешно добавлен.')
#     if d == 'найти':
#         h = input('Имя контакта: ')
#         if h in contacts:
#             print(contacts[h])
#         if h not in contacts:
#             print('Такого контакта не существует.')

scores = {

}
while True:
    a = input('Введите команду: ')
    if a == 'создать':
        last_name = input('Фамилия ученика: ')
        score = int(input('оценка: '))
        if last_name not in scores:
            scores[last_name] = score
        else:
            print('Ученик с такой фамилией уже есть в журнале.')
    if a == 'показать':
        g = input('Фамилия ученика: ')
        if g in scores:
            print(scores[g])
        if g not in scores:
            print('Такого ученика нет.')