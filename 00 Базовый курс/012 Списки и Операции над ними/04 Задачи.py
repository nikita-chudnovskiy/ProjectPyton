# К каким типам данных относится список?  [ ]   list()
# 8 11 3
print(list(map(int,input().split())))

#
a =["Тверь", "Уфа", "Москва", "Казань"]
print("Москва" in a)


#Подвиг 5. По какому индексу можно обратиться к значению 5 списка:

a = [0, True, "Москва", 5, False, "Омск"]
print(a[3],a[-3])
cities =["Тверь", "Уфа", "Москва", "Казань"]
print(cities[-1])

#Необходимо вычислить средний балл и вывести его на
#экран с точностью до десятых (один знак после запятой).
#3 3 2 4 4 5 4 3 2
marks = list(map(int, input().split()))
print(round(sum(marks)/len(marks),1))



# Мастер и Маргарита
# Булгаков
# 233
# 435.45
book =[input(),input(),float(input()),float(input())]
del book[2]
book[1]="Пушкин"
book[2] =book[2]*2
print(book)

#
# 52 65 64 54 68 59 42 63
# Sample Output:
# 68 42 467

s1=list(map(int,input().split()))
print(max(s1),min(s1),sum(s1))

# Sample Input:
#
# 52 65 64 54 68 59 42 63
# Sample Output:
#
# 68 65 64 63 59 54 52 42


a =list(map(int,input().split()))
a=sorted(a)
a=a[::-1]
print(*a)


cities = ["Москва", "Тверь", "Вологда"]
s1=input().split()
lst = ["Москва", "Тверь", "Вологда"]
print(*(lst+s1))






