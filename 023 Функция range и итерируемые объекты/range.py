# С помощью функии range можно сформировать конечную арифметическую прогрессию
print(range(5))
print(list(range(5))) # функиця арифметическая прогрессия   [0, 1, 2, 3, 4]
print(list(range(10,20)))# Задаем от  и до какого           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(10,20,2)))  # задаем шаг                   [10, 12, 14, 16, 18]

print(list(range(10,0,-1)))  # В обратном порядке
print(sum(range(1,5))) # Сумма всех чисел 1 до 5

print(len(range(5,15,5))) # Сколько чисел в нашей последовательности от 5 до 5 с шагом 5 (2)

a,b,c = range(7,10) # присвоение
print(a,b,c)
n,m,c =1,2,3
print(n,m,c)
a,b,c=map(int,input())
print(a,b,c)

r =range(1,5)
print(r)
print(r[1])# Итерируемый объект это такой объект который предостовляет возможнность поочередного прохода по своим элементам

n =iter([43,True,22]) # Список этерируемы
print(next(n))
print(next(n))
print(next(n))

n = iter('ADA')
print(next(n))
print(next(n))
print(next(n))
