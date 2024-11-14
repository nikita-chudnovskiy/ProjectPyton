# diamonds = 5
# redstouns = 3
# gold = 7
# for i in range(7):
#     a = input()
#     if a == 'add':
#         print('What?')
#         b = input()
#         if b == 'diamonds':
#             print('How Much?')
#             s = int(input())
#             diamonds = diamonds+s
#         if b == 'gold':
#             print('How Much?')
#             s = int(input())
#             gold = gold+s
#         if b == 'red stouns':
#             print('How Much?')
#             s = int(input())
#             redstouns = redstouns+s
#         if b != 'diamonds' and b != 'gold' and b != 'red stouns':
#             print('Unkown resourse')
#     if a == 'info':
#         print(diamonds,gold,redstouns)
#     if a == 'reset':
#         diamonds = 5
#         redstouns = 3
#         gold = 7
s = 0
for i in range(100):
    a = int(input())
    s = s+1
    if a == 0:
        break
print(s)

