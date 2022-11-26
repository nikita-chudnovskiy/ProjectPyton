import random
a =[]
for i in range(20):
    a.append(random.randint(-10,10))
count = [0]*21 # Тк нужен 0 то -10 10 20 и еще 0 ТО пишем 21 Урок 27

for i in a:
    count[i+10]+=1 # смещение
print(a)
for i in range(21):
    if count[i]>0:
        print(i-10,count[i])

        # При больших диапазонах не целесообразно будет съедать очень много памяти
