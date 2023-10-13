
class Point:

    color ='red'
    circle = 2
    def __init__(self, x=0, y=0): # Можжно создать без аргументов будет тк x= 0 y = 0
        self.x = x
        self.y = y

    def __del__(self):
        return print('Удаление '+ str(self))
    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return (self.x,self.y)

pt =Point(1,2)
print(pt.__dict__)

