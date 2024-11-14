# d = 0
# while True:
#     a = input()
#     d = d+1
#     if a == 'stop':
#         print(d-1)
#         break

bank = 10000
d = 0
while True:
    d = d+1
    a = input()
    if a == 'stop':
        break
    if a == 'add':
        s = int(input())
        bank = bank+s



