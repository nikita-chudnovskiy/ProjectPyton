# import random
# b = '1234567890ёйцукенгшщзхъфывапролджэячсмитьбю'
# g = int(input())
# for i in range(g):
#     a = random.randint(0,len(b)-1)
#     print(b[a],end='')

a = input()
print(a[-1]+a[:-1])