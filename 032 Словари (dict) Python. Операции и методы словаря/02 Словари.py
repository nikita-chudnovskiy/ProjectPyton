
d = {
        1:   45,
        'two':  'two',
        3:  [1,2,3,] # Ключем не может быть изменяемый тип объекта, такой тип список. ключ[1,2,3]: так нельзя
}
print(d)

# К словарю можно обращатся по ключу

print(d[1])

# Как добавить ключ - несуществующему ключу добовляем новое значение

d[4] ='four'
print(d)
print(d[4])

d['five']=5
print(d)