import random
# a = 'adadfafsdf234235fsdfds'
# for i in a:
#     if i.isalpha():
#         print(i,end='')
# print()
#
# b = [i for i in a if i.isalpha()] # Проверка на цифры и перевод в int
# print(b)



n =3
m = 3

c = [[0]*m for i in range(n)]
print(c)

for i in c:
    print(i)

print()
a = [[random.randint(1,99) for i in range(m) ] for j in range(n)]


for i in a:
    print(i)
print()

a = [[i*j for i in range(1,m+1) ] for j in range(1,n+1)]


for i in a:
    print(i)

a= [random.randint(1,10) for i in range(10)]
print(a)




# for j in range(1,10):
#     for i in range(1,10):
#         print(i,' * ', j , '=', i * j,'  ', end = ' ')
#     print()
