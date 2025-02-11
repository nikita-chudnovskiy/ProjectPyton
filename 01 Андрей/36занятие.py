f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if len(i) == 2:
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) > 2 and i[2] == 'н':
#         print(i)

text = text.lower()
for i in text:
    if i not in 'йцукенгшщзхъфывапролджэячсмитьбюё -':
        text = text.replace(i,'')
words = text.split()
print('Введите слово:')
a = input()
use = []
while True:
    use.append(a)
    last = a[-1]
    if last == 'ь':
        last = a[-2]
    for a in words:
        if a not in use and a[0] == last:
            print(a)
            use.append(a)
            last = a[-1]
            if last == 'ь':
                last = a[-2]
            print('Введите слово на букву',last)
            break
    a = input()
    if a[0] != last:
        print('Ваше слово начинается на не правильную букву, вы проиграли')
        break
    if a in use:
        print('Это слово уже использовалось, вы проиграли')
        break
