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

i = 0
str1 = 'javatpoint'

while i < len(str1):
    if str1[i] == 't':
        i += 1
        break
    print('Current Letter :', str1[i])
    i += 1