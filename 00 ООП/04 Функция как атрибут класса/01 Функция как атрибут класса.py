class Car:
    model = "BMW"
    engine = 1.8
    @staticmethod
    def drive():
        print("Let's go")
Car.drive()
print()
print(Car.__dict__)
a=Car()
print(a.__dict__)
a.drive()





