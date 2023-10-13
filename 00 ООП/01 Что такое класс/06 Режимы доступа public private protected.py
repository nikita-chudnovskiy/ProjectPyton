# Механизм Инкапсуляции

class Point:
    """
      attribute   public
     _attribute   protected  служит для обращения внутри клаасса и во всех дочерних
    __attribute   private    служит для обращения только внутри класса
    """
    # Класс единое целое к нему стоит обращатся через публичные методы set и get
    def __init__(self,x =0,y =0):
        self.__x = x
        self.__y = y   # лишь сигнализирует но не ограничивает доступ из вне через сылку экзэмпл класса будет доступно
                      # лишь предостерегает программиста
    def set_coord(self,x,y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x ,self.__y


pt =Point(1,2)
pt.set_coord(10,20)
print(pt.get_coord())


