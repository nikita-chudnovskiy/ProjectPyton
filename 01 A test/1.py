# def ZnacenieBolshe10(x):
#     return x>10
#
#
# a = [2,11,12,14]
#
# a=list(filter(ZnacenieBolshe10,a))
# print(a)
#
b =[]
c =[2,3,5,11,12,44,47]
for i in range(len(c)):
    if c[i]<10  or c[i]<45:
        b.append(c[i])
print(b)

a =[i for i in c if i <=10]
print(a)