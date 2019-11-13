# while
number = int(input())       # Стадион Пока я БОДРЕНЬКИЙ Я БЕГУ

#Заголовок цикла	
while number <=10:     		# ПОКА number <=10 то Цикл будет выполнятся  !!!   # Если +=2 , Ввести 1 то все нечетные 1 - 10  , все четные если ввести 2
	print('Число ',number ) # ТЕЛО ЦИКЛА  Список Инструкций
	number +=1	# +=2		# ТЕЛО ЦИКЛА  Список Инструкций     ( Одно действие, ПРЕВАЯ ИТЕРАЦИЯ)

# Оператор if Добавили Цикл while

print('Привет как тебя зовут')
name = input()
number = 6
yes = True
print ('Сколько тебе лет ', name)

while yes:
    age = int(input())
    if age == number:
        print('да верно !')
        yes = False       # это останавливает цикл while    # Можно просто break тогда не выполнится последнее else
    elif age < number:
        print('Чуть больше')
    else:
        print('Чуть меньше')
else :
    print('Ты угадал')



