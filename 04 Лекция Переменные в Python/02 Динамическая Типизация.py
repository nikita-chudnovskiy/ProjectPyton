# Оперативная память там лежат объекты

bambulbe = 'Шмель'
print(bambulbe)
# Изменили значение Динамическая типимизация
bambulbe = 'Муха'
print(bambulbe)

# Переменная переменяет свое значение
my_car = 'Тойота RAW4'
my_car = 4
print(my_car)
print(type(my_car))

# isinstance функция, являеся ли объект my_car str
print(isinstance(my_car, str))

# У каждого объекта свой id
print(id(bambulbe))
print(id(my_car))
print()

my_jip = my_car
print(id(my_jip), id(my_car))
print(id(my_jip) == id(my_car))
