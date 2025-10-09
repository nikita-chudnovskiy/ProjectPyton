# f = open('kd.txt','r',encoding = 'utf-8')
# text1 = f.read()
# f.close()
#
# words = text1.split()
# for i in words:
#     if i[0] == 'к' and i[-1] == 'а' and len(i) > 1:
#         print(i)

# def common_letters(e,u):
#     g = 0
#     for i in e:
#         if i in u:
#             g = g+1
#     return(g)
#
# w = common_letters('Автобус','Арбуз')
# print(w)

# def is_anagramm(j,l):
#     for i in j:
#         if i in l:
#             continue
#         if i not in j:
#             return(False)
#         if i not in l:
#             return(False)
#     return(True)
#
# h = is_anagramm('Корабль','бКольра')
# print(h)