def message(number):
    def print_message():
        return 'число '+str(number)
    return print_message()
print(message(2))




# Замыкание это сохранение состояния с помощью внутренних функций
# При помощи замыкания после завершения работы функции локальные переменные не уничтожаются а будут сохранятся до след запуска этой функции
# Локальная переменная не уничтожится если на нее осталась живая ссылка
def message(x):
    def print_message(y):
        return x,y
    return print_message
d =message(4) # Запомнил 4
print(d(8))
print(d(10))