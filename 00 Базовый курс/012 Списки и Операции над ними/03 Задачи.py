# В списке найти 20 и заменить на 200
a = [1, 2, 20, 20]
print(a.index(20))  # Ищет 1 вхождение
print(a)
a[2] = 200
print(a)

# Убрать пробелы
spisok1 = ["Привет", "", "sdsd", ""]
spisok2 = list(filter(None, spisok1))
print(spisok2)

# Возвести в квадрат
a = [2, 4, 6, 8]
s1 = [i * i for i in a]
print(s1)

# Убрать 20,99,6
spisok1 = [99, 2, 3, 20, 20, 20, 4, 5, 6]
print(spisok1)

spisok2 = [i for i in spisok1 if i != 20 and i!=99 and i!=6]
print(spisok2)
spisok2 = spisok2[::-1]
print(spisok2, " Перевернули")

#
# list1 = [(1,2),(7,7)]
# for a,b in list1:
#     print(a+b)
