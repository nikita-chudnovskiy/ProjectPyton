# b = 0
# while True:
#     a = int(input())
#     if a > b:
#         b = a
#     if a == 0:
#         break

s = 0
number = 0
while True:
    a = int(input())

    if a == 0:
        break
    if a > 4:
        number = number+1
        s +=a

print(s,number)