# Механизм Инкапсуляции
#from accessify import private,protected  дполнительный модуль защиты обращения к мотоду
class Point:
    """
      attribute   public
     _attribute   protected  служит для обращения внутри клаасса и во всех дочерних
    __attribute   private    служит для обращения только внутри класса
    """
    # Класс единое целое стоит взаимодействовать с ним  только через публичные свойства и методы set и get
    def __init__(self,x =0,y =0):
        self.__x = self.__y=0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
     #private
    @classmethod
    def __check_value(cls,x):
        return type(x) in (int ,float)

    def set_coord(self,x,y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами')

    def get_coord(self):
        return self.__x ,self.__y

pt =Point(1,2)
pt.set_coord(10,'10')
print(pt.get_coord())

#print(pt.__x) доступа не будет


