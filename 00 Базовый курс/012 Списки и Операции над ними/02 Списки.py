import math
print()
goroda =["Москва","Санкт-Питербург","Нижний-Новгород"]
print("Выбрали город под индексом 0",goroda[0])

# Список динамически изменяемый обьект в отличии от строк и чисел
ocenki = [4,2,3,4,5,3]
#         0,1,2,3,4,5  индексы
#        -6-5-4-3-2-1  и в обратном порядке можно обращатся
print("Средний бал: ",sum(ocenki)/len((ocenki)))


ocenki[1]=5
ocenki[2]="Удовлетворительно"
print(ocenki) # Ученик исправил отметку
print(ocenki[-6]) # Оценка 4

# Списки могут содержать разные типы данных и любой другой тип данных (любые обьекты)

a=[1,2,3]
spisok = [1,'Привет',True,a,5.8,False] # Даже список
print(spisok)

# Можно записать так

b = list(["Hello",True,False])
print(b)

a=list("python")
print(a)

# Основные методы
#    len(a),max() , min(),sum()sorted(),
#    + соединение двух сисков
#    * Дублирование
#    in вхождение
#    del удаление

f =[5,2,3,9,7,4,8,2]
#список можно сортировать и с помощью метода sort и с помощью функции sorted.
#Разница только в том, что метод sort не создает новой коллекции, а меняет уже
# существующую. Функция же sorted не меняет
#сходную коллекцию, а создает новую с отсортированными элементами. Поэтому,
#для изменения коллекции a здесь следует записывать такую конструкцию: