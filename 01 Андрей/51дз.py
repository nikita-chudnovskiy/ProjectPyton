# def count_2(text):
#     b = 0
#     for i in text:
#         if i == 'а':
#             b = b+1
#     if b == 2:
#         return(True)
#     else:
#         return(False)
#
# s = count_2('Я пошел в магазин что бы купить еду')
# print(s)

def average(numbers):
    s = sum(numbers)
    return(s/len(numbers))
#
# d = average([5,1,7,2])
# print(d)

def above_average(ot):
    b = []
    a = average(ot)
    for i in ot:
        if i > a:
            b.append(i)
    return(b)
sd = above_average([2,1,6,9,3])
print(sd)