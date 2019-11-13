# Метод format
age = 33
name = 'Никита'
print('Меня зовут  {0} -- {1}   лет.'.format(name, age))
print('Почему забавляется {0}  c этим Python ?'.format(name))

# >>> # десятичное число (.) с точностью в 3 знака для плавающих:
print(' Проверка {0:.3}'.format(1 / 3)) # '0.333'

# >>> заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('Andrey'))  # '___hello___'

#  >>> # по ключевым словам:
# >>> 'Swaroop написал A Byte of Python'
print(' {name} написал {book} '.format(name='Swarop', book='A Byte of Python'))





## https://www.python.org/dev/peps/pep-3101/
