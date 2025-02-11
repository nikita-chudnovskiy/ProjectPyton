# countries = {
#     "Россия": "Москва",
#     "Франция": "Париж",
#      "Италия": "Рим"
# }
# print('Введите страну:')
# a = input()
# if a in countries:
#     print('Столица:',countries[a])
# if a not in countries:
#     print('Такой страны нет в словаре')

# d = {
#
#
# }
# print('Введите предмет:')
# a = input()
# print('Введите цену:')
# b = int(input())
# if b not in d:
#     d[a] = b
# print('Словарь:',d)

products = {
    "яблоко": 50,
    "банан": 30,
    "хлеб": 40
}
print('Введите товар:')
a = input()
print('Введите количество товара:')
b = int(input())
f = products[a]*b
print('Стоимость:',f)