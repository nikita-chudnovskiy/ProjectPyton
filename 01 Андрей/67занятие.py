# names = ['Саша','Паша','Аня','Андрей']
# last_names = ['Коротков','Игрушов','Иванова','Менданов']
# r = input()
# for idx in range(0,4):
#     if names[idx] == r:
#         print(last_names[idx])

# names = ['Саша','Паша','Аня','Андрей']
# last_names = ['Коротков','Игрушов','Иванова','Менданов']
# scores = [79,64,56,81]
# d = input()
# for idx in range(0,4):
#     if last_names[idx] == d:
#         print(names[idx],scores[idx])

# alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# t = input()
# for idx in range(0,33):
#     if alf[idx] == t:
#         print(alf[idx+1])

f = open('kd.txt',encoding='utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if 'ъ' in i:
#         print(i)

# words = text.split()
# for i in words:
#     if i[0:3] == 'при':
#         print(i)