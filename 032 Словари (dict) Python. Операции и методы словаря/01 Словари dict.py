# Словари сокращенно (dict) dictionary

# Словарь - не упорядоченная коллекция произвольных объектов с доступом по ключу


a =['Moskow','Piter','Penza']
print(a)

# Moskow - 495
# Piter  - 812
# Penza  - 8412

#  key: value
# ОСНОВНОЙ СПОСОБ СОЗДАНИЯ СЛОВАРЯ
print('ОСНОВНОЙ СПОСОБ СОЗДАНИЯ СЛОВАРЯ')

b={}
d ={
    'Moskow': 495,
    'Piter':  812,
    'Penza':  8412

}
print(d)

print()
# Второй способ только если ключ строка
r =dict(moskow=495,piter=812,penza=8492)
print(r)

# 3 Способ создания словаря
b =[[1,495],['Piter',812],['Penza',8412]]
b=dict(b)
print(b)


# 4 способ  dict.fromkeys

q = dict.fromkeys(['a','b','c',],100)
print(q)

q={}  # Пустой словарь
print(type(q))