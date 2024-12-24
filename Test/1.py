# a, b, c = str(input()), str(input()), str(input())
# print(min(a, b, c, key=len ))
# print(max(a, b, c, key=len ))

my_list=['Москва','Санкт-Питербург']
print(max(my_list, key=len, default=''))
print(min(my_list, key=len, default=''))


a = input()
b = input()
c = input()
if min (len(a), len(b), len(c)) == len(a):
    print(a)
elif min (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max (len(a), len(b), len(c)) == len(a):
    print(a)
elif max (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)