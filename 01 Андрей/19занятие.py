# a = [1,2,3,4,5]
# print(a[1:4])
# print(a[:3])
# print(a[2:])
# print(a[:])

# b = [7,16,9,1]
# for i in b:
#     print(i)

# a = []
# for i in range(5):
#     b = input()
#     a.append(b)
# f = input()
# flag = False
# for i in a:
#     if i == f:
#         flag = True
# if flag == False:
#     print('Нету')
# if flag == True:
#     print('Есть')

# a = []
# for i in range(5):
#     b = input()
#     a.append(b)
# f = input()
# if f in a:
#     print('Есть')
# else:
#     print('Нету')

g = []
a = []
for i in range(5):
    b = input()
    a.append(b)
for i in range(5):
    x = input()
    g.append(x)
for i in a:
    if i in b:
        print(i)