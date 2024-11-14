# s = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     if a > 10:
#         s = s+1
# print('Количество чисел > 10:',s)

n = None
while True:
    b = int(input())
    if b == 0:
        break
    if n == None:
        n = b
    if b > n:
        n = n
    if b < n:
        n = b
print("Минималльное число:",n)