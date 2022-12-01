
class Car:
    model = "BMW"
    engine = 1.8
a1 = Car()
a2 = Car()

print(Car.__dict__)

print(a1.__dict__)
a1.model='Lada'
print(a1.__dict__)


print(a2.engine)
print(Car.model)