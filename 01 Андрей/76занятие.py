import random
allnames = ["Алексей", "Иван", "Дмитрий", "Сергей", "Андрей", "Максим", "Никита", "Владимир", "Павел", "Егор"]
allsurnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Морозов", "Смирнов", "Попов", "Васильев", "Соколов", "Михайлов"]
names = []
surnames = []
ages = []
for i in range(1000):
    h = random.randint(0,9)
    name = allnames[h]
    b = random.randint(0,9)
    surnames = allsurnames[b]
    age = random.randint(0,100)
    print(name,surnames,age)