class Point:

    "__new должен возвращать адрес нового обьекта"
    def __new__(cls,*args,**kwargs):
        print('метод __new'+ str(cls))
        return super().__new__(cls)

    def __init__(self,x,y):
        print("Вызов __init__"+str(self))
        self.x = x
        self.y = y


pt =Point(1,2)
pt1 =Point(2,2)

print(pt)
print(id(pt))
print(id(pt1))