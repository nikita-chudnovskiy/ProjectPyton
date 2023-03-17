# # Найти все индексы ра
# text = input().lower()     # Получаю строку и перевожу все символы в нижний регистр
# res_count = 0              # Сюда буду записывать индексы
# if 'ра' in text:           # Проверяю есть ли вообще в переданном тексте сочетание букв 'ра', если нет то работа программы не имеет смысла
#     for i in range(0, text.count('ра')): # Перебираю текст циклом для нахождения всех индексов, text.count('ра')
#         # - вернет сколько раз встречается 'ра' в тексте, чтобы цикл не делал лишней итерации
#         if 'ра' in text:   # Проверяю есть ли в переданном тексте сочетание букв 'ра', для вывода индекса
#             res_count = text.find('ра', res_count if i == 0 else res_count + 1) # Если нахожу сохраняю в переменную, res_count + 1 использую
#             # для дальнейшего прохода, иначе будет находить все время одни и тот же индекс.
#             print(res_count, end=' ')     # Вывожу результат
# else:
#     print('-1')     # проверка не пройдена возвращаю -1

s = 'баРАбанщик бил бой в барабан'

# def find_index(input_str, search_str):
#     l1 = []
#     length = len(input_str)
#     index = 0
#
#     while index < length:
#         i = input_str.find(search_str, index)
#         if i == -1:
#             return l1
#         l1.append(i)
#         index = i + 1
#     return l1
#
#
# print(*find_index(s, 'ра'))

#Источник: https://pythonim.ru/string/metod-find-python

s=input()
if not 'ра' in s:
    print(-1)
else:
    for i in range(len(s)-1):
        if s[i]=='р' and s[i+1]=='а':
            print(i,end=' ')
