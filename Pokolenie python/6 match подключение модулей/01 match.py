import math

print(math.sqrt(16))  # пишем всегда match
import math as m

print(m.sqrt())  # сократили

from math import * # можно писать без match

# Однако рекомендуется избегать импортирования через from math import *, так как нет ясности,
from math import sqrt,factorial

print(sqrt(),factorial())

"""
над тем, какие функции доступны в вашем коде.
Вместо этого рекомендуется использовать # import math или from math import sqrt, pi,#  чтобы явно указать, 
какие функции или переменные вы хотите импортировать. Это делает ваш код более читаемым и уменьшает вероятность конфликтов имен.
"""