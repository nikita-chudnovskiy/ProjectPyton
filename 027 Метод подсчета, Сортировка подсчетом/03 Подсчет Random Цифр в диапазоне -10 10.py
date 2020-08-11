import random
a =[]
for i in range(10):
    a.append(random.randint(-5,5))
count = [0]*11 # Тк нужен 0 то -10 10 20 и еще 0 ТО пишем 21 Урок 27

for i in a:
    count[i+5]+=1
print(a)
for i in range(11):
    if count[i]>0:
        print(i-5,count[i])

        # При больших диапазонах не целесообразно будет съедать очень много памяти
