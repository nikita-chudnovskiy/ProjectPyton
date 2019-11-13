print('Привет как тебя зовут')
name = input()

print('Рад познакомится' , name)
 
age = int(input('Сколько тебе лет, ' + name + '?'))
print('А я думал тебе ', age + 1, end ='')
x = age + 1 #для 100 x = age+1%100

#  if  УСЛОВИЕ : 				Может быть довольно длинным . может быть вызов функции 
if x >= 11 and x <= 19: 
    print('лет') # Блок кода 4 пробела
elif x % 10 == 1:	
	print(' год ')
elif  x % 10 >= 2 and x % 10 <= 4:
	print(' года ')
else:
	print(' лет ')
	print(' !...')



