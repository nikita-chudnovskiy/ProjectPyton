class Vector:
    MIN_CORD = 0
    MAX_CORD=100

    @classmethod              # classmethod работает только с атрибутами класса
    def validate(cls,arg):
        return cls.MIN_CORD<= arg <=cls.MAX_CORD

    def __init__(self, x, y):
        self.x =self.y =0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_cord(self):
        return self.x, self.y

    @staticmethod                # Статич метод предпологается исп только с этими параметрами x ,y
    def norm2(x,y):
        return x**2 + y**2

v = Vector(1,200) # Поставили не допустимое значение Выдаст (0,0)
res =v.get_cord()
print(res)

print(v.validate(1111))
print(Vector.norm2(2,5))