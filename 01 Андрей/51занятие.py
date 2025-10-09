# def warden(slovo):
#     if slovo[0] == slovo[-1]:
#         return(True)
#     else:
#         return(False)
# a = input()
# fd = warden(a)
# print(fd)

# def reid(numbers):
#     d = []
#     for i in numbers:
#         if i > 5:
#             d.append(i)
#     return(d)
#
# s = reid([2,13,23,7,45,3,8])
# print(s)

# def abreveit(dsf):
#     for i in dsf.split():
#         print(i[0],end='')
#
# abreveit('Международная космическая станция')

def textr(text):
    for i in text.split():
        if len(i) > 2:
            print(i,end=' ')

textr('Я пошёл в школу')