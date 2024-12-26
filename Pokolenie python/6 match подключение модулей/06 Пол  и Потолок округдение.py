from math import floor, ceil  # fllor внииз поо ceil вверх потолок

x = float(input()) # 5.5, 5.1 , 5.4, -12.2 ( если 12 то округлять нечего 24 )
# print(floor(x))  # 5
# print(ceil(x))  # 6
print(ceil(x) + floor(x))


