# Zip iter 1, iter 2 (a,b)

a =[1,2,3,4]
b =[100,200,300,400]
c ='abcd'
for i in range(4):
    print(a[i],b[i])


rez =list(zip(a,b,c)) # Если списком не сделать то обойти итератор можго только 1 раз
print(rez)


for i in rez:
    print(i)

print('___________')
for i in zip(a,b,c):
    print(i)


print('___________')
for t1,t2,t3 in zip(a,b,c):
    print(t1,t2,t3)


# Распаковка

col2,col2, col3 = zip(*rez)
print(rez)