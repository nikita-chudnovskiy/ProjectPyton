def first_letter_a(text):
    d = []
    for i in text.split():
        if i[0] == 'а':
            d.append(i)
    return (d)
# g = first_letter_a('На столе лежит абрикос и ароматный кофе')
# print(g)

def last_letter_c(c):
    c2 = []
    for i in c:
        if i[-1] == 'с':
            c2.append(i)
    return(c2)
#
# d = last_letter_c(['алекс','очень','любит','кушать','абрикос','и','ананас'])
# print(d)

def first_a_last_c(text):
   d1 = first_letter_a(text)
   d2 = last_letter_c(d1)
   return(d2)
s = first_a_last_c('атлас показывает страны, а абакус упрощает подсчеты в уме')
print(s)