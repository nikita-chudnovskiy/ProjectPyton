class Car:
    model = "BMW"
    engine = 1.8

    def drive():
        print("Let's go")
Car.drive()

print(Car.__dict__)
a=Car()
print(a.__dict__)

print(a.drive()) # Ругается тк в классе !!! в функции должно быть параметры функции

