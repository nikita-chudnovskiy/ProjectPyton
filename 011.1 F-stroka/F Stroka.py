# name = 'Андрей'
# age = 18
#
# print(f"{name},{age}")
z=['Петров','Иван',23]

n,m,b =z # n 0 m 1 b 2 Распаковка См видео
print(n,m,b)
print()


goda = {
        1:'Год',
        2:'Года',
        3 :'Лет'
}

dorog= {
        1:'Дорогой',
        2: 'Дорогая'
}



spisok = [
    [1,'Иванов', 'Василий', 38,3],
    [2,'Иванова', 'Анастасия', 32,2],
    [1,'Иванов', 'Александр', 1,1],
    [2,'Иванова', 'Анастасия', 2,2],
    [2,'Иванова', 'Екатерина', 1,1]
]
f =[]
for z,midlname, name, age,g in spisok: # Работа с ключами и подстановками
   print(f"{dorog[z]},{midlname},{name},{age},{goda[g]}")


