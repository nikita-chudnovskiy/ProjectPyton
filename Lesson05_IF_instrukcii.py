# Оператор if
years = 33

number = int(input('Введите Сколько Вам лет : '))

if number == years : #ЕСЛИ
    print('Да Вы угадали '+str(number))
    if years <= 34:                 # Вложенная еще 1 проверка
        print(str(number) +" Да и это верно  меньше 35 ")
elif number < years:
    print('Чуть больше ')
# Внутри блока вВы можете выполнять все что угодно
else:                       #ИНАЧЕ
    print('Чуть меньше ')
    print('Завершено ')
# чтобы попасть сюда, number должно быть больше, чем years

# Помните, что части elif и else не обязательны. Минимальная корректная за-пись оператора if такова:
if True : # 2 == 2
    print('верно.{0:_^11}'.format(years))


print('hi')
print(he)


		 
 


