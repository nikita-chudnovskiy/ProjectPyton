def min2(d,a):
    if d > a:
        return(a)
    if a > d:
        return(d)
    if a == d:
        return(d)
# F = int(input())
# J = int(input())
#
# e = min2(F,J)
# print(e)

# def min4(q,w,e,r):
#     qw = min2(q,w)
#     er = min2(e,r)
#     return(min2(qw,er))

# s = min4(9,2,13,8)
# print(s)

# def count(s):
#     b = 0
#     for i in s:
#         if i == 'а':
#             b = b+1
#     return(b)
# w = input()
# d = count(w)
# print(d)

# def mylen(xd):
#     f = 0
#     for i in xd:
#         f = f+1
#     return(f)
# df = mylen('В актовом зале начался спектакль')
# print(df)

def rare(door,fg):
    b = 0
    for i in door.split():
        if i == fg:
            b = b+1
    return(b)
f = open('kd.txt',encoding='utf-8')
text = f.read()
f.close()

a = rare(text,'небо')
print(a)