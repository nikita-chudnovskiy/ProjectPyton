a =[1,1,2,3,5,4]  # от 0-5 6 значений
count =[0]*6 # Создаем список из 6 Нулей (0)   ( 0 левой эл будет отв за колч 0 в этом списке 1 за количе 1 2 заколич 2 и т д
#  6 элемент за количество 5 ерок в этом списке

for i in a:
    count[i]+=1 # Будет накапливатся количество нашего элемента
print(a)
for i in range(6): # 6  длинна count 6
    if count[i]>0:
        print(i,count[i])
        #print((str(i) + ' ') * count[i], end=' ')
