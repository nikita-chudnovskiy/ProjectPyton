


a = [10,20,30]
b = 'hello'
c =(79,89,99)

d = {'a':1,'b':2,'c':3} # Только ключи покажет и лучше не использовать не упорядочная коллеуия


for index,value in enumerate(a):
    #a[index]+=1 при таеком варианте знаение списка изменится
    print(index,value)
print()

for i,v in  enumerate(b,100): # Нумерация с 100
    print(i,v)

print()

for i ,v in enumerate(c):
   print(i,v)


print()
for i,v in enumerate(d):
    print(i,v)


k =['z','g','l']

print()
for i in range(len(k)):
    print(i,k[i])
