class Cat:
    # Данные (свойства - атрибуты)
    # Инкапсуляция это скрытые данные и методы из вне !!!
    poroda = 'Siamskiy'
    name = 'Вася'
    age =20

    def go(self):
        print("Кот может бегать")



cat1 =Cat() # Эказемплры классса
print(cat1.go())

cat1.name ='Бытряк'
cat1.poroda ='Sibirskiy'
cat1.age=10
print(Cat.name)


