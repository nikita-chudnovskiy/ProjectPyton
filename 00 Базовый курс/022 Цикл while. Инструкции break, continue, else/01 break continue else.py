# break досрочное завершение цикла
# continue пропуск одной итерации цикла
i = 0

d =[1,2,3,4,5,6]
print("Начало цикла")
while i<len(d):
    if d[i]%2==0:
         print(d[i])
    if d[i] ==5:
        break

    i += 1





# Continue
str = "JavaTpoint"
i=0
while i <len(str):
    if str[i]=="T":
        i += 1
        continue

    print(str[i])
    i += 1
