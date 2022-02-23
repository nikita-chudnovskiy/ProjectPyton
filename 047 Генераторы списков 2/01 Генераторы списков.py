a = [
    ('Lidorov',1995),
    ('Ietrov',2000),
    ('Kasilev',1988),
    ('Eoznik',2010),
    ('Hlebov',2021),
    ('Slepov',2020),
]




b =[elem for elem in a ]
print(b)


b =[elem[0][0] for elem in a if elem[1]<2011 ]
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