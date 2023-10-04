
class Point:
    def __init__(self, x, y): # Можжно ghbcdjbnm x= 0 н = 0
        self.x = x
        self.y = y


p1 = Point(1,2)# если  выше присвоить x = 0 y = 0 b и не задать Point() будут 0
print(p1.__dict__)