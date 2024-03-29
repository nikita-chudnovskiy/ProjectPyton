# Функция print() print(value, ..., sep=' ', end='\n')
# Внутри функции print() нужно передать одно или несколько значений через запятую.


a,b,c, =1,2,3
a =b =c =3
print(a,b,c)

x,y,z =map(int,input().split())
print(x,y,z)

# Вввод список
a =list(range(0,10))
print(a)
a =list(range(9,-1,-1))
print(a)



print(1234)
print(1,2,3,4)
print('hello',True,21)
print(2+3,4*5,2+3*4)

a = 100
b = 200
print(a, '+', b, '=', a + b)

# В пределах одной команды print() все значения будут выводиться по умолчанию в одну строчку через пробел.
# Символ, который выводиться между значениями, называется разделителем (от англ. "separator").
# Как я уже писал ранее по умолчанию разделитель равен знаку пробел.
# Но это поведение можно изменить при помощи параметра sep.
# Ему нужно присвоить внутри функции print() новое значение типа строки.
print(1,2,3,4)
print(1,2,3,4,sep=' ')
print(1,2,3,4,sep='')
print(1,2,3,4,sep=',')
print(1,2,3,4,sep='*')



print(1, 2, 3, sep=',') # sep разделитель разделяет запятой
print(4, 5, sep='???', end=',') # sep разделяет ??? end (не  переводит на следующую строку 6)
print(6,7, sep=',')  # Нужно как минимум 2 значения


rub = 10
kop = 99
print('У меня есть %s рублей %s копеек' % (rub, kop))

rub,kop = map(int,input().split())
print('Нам дали {} рублей {} копеек'.format(rub,kop))