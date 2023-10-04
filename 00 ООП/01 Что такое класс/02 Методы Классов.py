class Point:
    "class"
    "свойста  атрибуты (данные)"  # Имена используют существительные            set_value get_param start stop
    "методы            (дейсствия)" # Имена Используют глаголы тк это действвие  color size x,y

    color = 'red'
    engin =2


    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return (self.x,self.y)


pt = Point()
pt2 = Point()
pt.set_cords(2,4)
pt2.set_cords(10,20)
print(pt.__dict__)
print(pt2.__dict__)


print(pt.get_cords())



