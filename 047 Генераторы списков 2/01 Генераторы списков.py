a = [
    ('Sidorov',1995),
    ('Petrov',2000),
    ('Vasilev',1988),
    ('Voznik',2014),
    ('Hlebov',1980),
    ('Slepov',2020),
]




b =[elem for elem in a ]
print(b)


b =[elem[0] for elem in a] # Сортировка по Имени
print(b)

b =[elem[1] for elem in a] # Сортировка по годам
print(b)


b =[elem[0] for elem in a if elem[0].startswith('S') or elem[0].startswith('H')] # Сортировка Все фамилии на S или H
print(b)

b =[elem for elem in a if elem[1]>2000] # Вывести всех старше 2000
print(b)
b =[elem[0] for elem in a if elem[1]>2000] # Вывести всех старше 2000
print(b)