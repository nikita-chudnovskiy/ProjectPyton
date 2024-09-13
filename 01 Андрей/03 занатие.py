# print('Введите номер месяца:')
# a = int(input())
# if a == 1:
#     print('Январь')
# if a == 2:
#     print('Февраль')
# if a == 3:
#     print('Март')
# if a == 4:
#     print('Апрель')
# if a >12 or a<1:
#     print('Неверный номер')

# a = int(input())
# b = int(input())
# if a<b:
#     print(a)
# else:
#     print(b)


print('Введите номер месяца')
a = int(input())
if a == 1:
    print('Январь 31')
if a == 2:
    print('Февраль 28')
if a == 3:
    print('Март 31')
if a == 4:
    print('Апрель 30')

if a <1 or a >12:
    print('Неверный номер')