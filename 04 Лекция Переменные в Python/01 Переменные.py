# Переменная это ссылка на объект

my_favorite ='Тойота RAW4' # переменная car - это ссылка на объект !

print('Объект',my_favorite,'c типом',type(my_favorite)) # У данного объекта Тойота raw 4 в данный момент тип Строка
# my_favorite = оператор присваивания, ( Связывание ИМЕНИ С ОБЪЕКТОМ) Имя может перепривязатся к другому обьекту

knight ='Рыцарь'        # Тем самым создали переменную с , ПЕРЕМЕННЫЕ Создаются в момент первого его присвоения
defender=knight
print()                 # 'Две переменные ссылаются на 1 объект'
print('2 переменные knight и defender',knight,defender)
car = my_favorite
print(car[-3])          # -3 это символ А с конца


# ИМЕНОВАНИЕ ПЕРЕМЕННЫХ ВАЖНАЯ ЗАДАЧА
# должны указывать на вид объекта
# Все буквы в нижнем регистре сat, knight
# Если несколько слов - отделять подчерками site_parser
cat ='Мурзик'
my_wife ='Юлия'

# Множественное присвоение

car = my_favorite = rav4 ='Тойота RAW4'

my_car, my_wife ='Тойота RAW4','Юлия'
print(my_car,my_wife)

x,y,z = 10,20,30
print(x,y,z)
x,y,z = my_car,20,30
print(my_car,y,z)
