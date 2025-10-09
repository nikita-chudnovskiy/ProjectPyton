# def iabloko(stroka):
#     b = 0
#     for i in stroka:
#         if i == 'а':
#             b = b+1
#     return(b)

# def qwerty2(df,s,u):
#     h = max(s,u)
#     import ainde52
#     s = ainde52.qwerty(df,h)
#     return(s)
# e = qwerty2([3,8,12,5,78],13,16)
# print(e)

def qwerty(dfg):
    return(dfg[::-1])

import ainde52
z = ainde52.qwerty([2,12,7,5],8)
print(z)
y = qwerty('я пошел в школу')
print(y)