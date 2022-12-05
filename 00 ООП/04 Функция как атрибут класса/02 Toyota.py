class Toyota:

    def __int__(self):
        self.color='Красный'
        self.speed = '200 км'
        self.engine = 0

    def start(self):
        print('Мотор запущен')
        self.engine = 2000

    def go(self):
        print("Поехали")
my_car =Toyota()
print(my_car.color)


