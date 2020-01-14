x1,x2 = map(float,input().split())
print(abs(x1-x2))

import math
#from math import *     Тут чтоб math не прописывать

x1,y1,x2,y2 = map(float,input().split())


def distance(x1, y1, x2, y2):
    c = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c

c = distance(x1, y1, x2, y2)
print(c)