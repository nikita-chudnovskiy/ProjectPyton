# обязательно пишем docsting к ффункциям к класса в определенных местах
import random


def random_list():
    """
    Функция возвращает рандомные значения от -10 до 10
    :param list a
    :return: a
    """

    a = [random.randint(-10, 10) for i in range(10)]
    return a

print(random_list())