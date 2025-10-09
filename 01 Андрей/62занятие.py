# def korablik(y):
#     for i in y:
#         if i in 'ёуеыаоэяию':
#             i = i*2
#             print(i,end='')
#         else:
#             print(i,end='')
#
# korablik('Сыро-капчёный')

# t = [5,9,2,16,32]
# h = int(input())
# index = 0
# for i in t:
#     if i == h:
#         print(index)
#         break
#     else:
#         index = index+1

# t = [5,9,2,16,32]
# h = int(input())
# for i in range(0,5):
#     if t[i] == h:
#         print(i)

t = [5,9,2,16,32]
h = int(input())
print(t.index(h))