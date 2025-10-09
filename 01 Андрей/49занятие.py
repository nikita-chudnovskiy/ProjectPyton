# def myf():
#     for i in range(10):
#         print('привет!')
#
# myf()
# myf()

# def mult2(a,b):
#     print(a*b)
#     print(a+b)
#     print(a-b)
#     print(a/b)
#
# mult2(7,6)
# mult2(20,10)

# def grusha(a):
#     b = 0
#     for i in a:
#         if i == 'о':
#             b = b+1
#     print(b)
#
# grusha('Сегодня очень тепло на улице')


# def maks2(g,c):
#     if g > c:
#         return(g)
#     if c > g:
#         return(c)
#     if c == g:
#         return(g)
#
# d = maks2(4,7)
# print(d)

# def contain(f,gyr):
#     if gyr in f:
#         return True
#     if gyr not in f:
#         return False
#
# rt = contain([2, 18, 7, 2],18)
# print(rt)

def rukzak(d):
    gh = []
    for i in d:
        if i < 5:
            gh.append(i)
    return gh

s = rukzak([4,8,29,3,84])
print(s)