# Напишите программу, в которой пользователь вводит слова. Пока эти слова начинаются на русскую букву «я»
# (заглавную либо строчную), программа работает. Как только происходит иное — завершает работу.
a = input()

while a>='я'or a>='Я':
    print(a)
    a =input()
