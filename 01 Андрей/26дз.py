# a = 100
# while True:
#     print(a)
#     a = a-1
#     if a == 0:
#         break

# b = []
# from random import randint
# for i in range(100):
#     a = randint(1, 500)
#     b.append(a)
# print(b)

b = []
less = []
greater = []
for i in range(6):
    a = int(input())
    b.append(a)
for i in b:
    if i <5:
        less.append(i)
    if i >=5:
        greater.append(i)
print('числа меньше 5:',less)
print('числа больше 5 или 5:',greater)