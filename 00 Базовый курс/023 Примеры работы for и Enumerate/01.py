n= int(input("Введите натуральное число от 1 до 100 "))

if n <1  or n>=100:
    print("Не верно введено число")

else:
    p=1
    for i in range(1,n+1):
        p=p*i
    print(f"Факториал {n}! ={p}")



for i in range(1,7):
    print('*'*i)

# 2 способа
words =["Python","дай","мне","силы","пройти","этот","курс","до","конца"]
print(*words)

print(" ".join(words))


digt = [1,2,66,-34,-12,-10]

for i, v in enumerate(digt):
    if digt[i]<=50:
        digt[i]=0
        print(i,v)
print(digt)

for i,v in enumerate(digt,100):
    print(i,v)

