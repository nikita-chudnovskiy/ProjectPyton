s = "python"
print(s.upper())            # Большие
print(s.lower())            # Маленькие
msg ="abracadabra"
print(msg.count("ra"))      # Найдем число вхождений в подстроку
print(msg.count("ra",4))    # Найдем подстроку c 4 индекса
print(msg.count("ra",4,10)) # Найдем подстроку c 4 индекса до 10 индекса

# msg ="abracadabra"
#       012345678910
print(msg.find("br"))               # Возвращает индекс первого вхождения
print(msg.find("bra",2,len(msg)))   # Найдем первое вхождение покажет индекс
print(msg.find("brr",2,len(msg)))   # Если не найдет то всегда -1
print(msg.rfind("br",4,11))         # Ищет справа налево

# Работает точно также как find - если нет то приводит к ошибке
#print(msg.index("brк",0,11)) # Ищет справа налево (Такие ошибки можно обрабатывать как исключения!!!) Важно


# replace Метод Замены old на new

msg ="abrakadabra"
print(msg.replace("a","o"))     # replace Метод Замены old на new
print(msg.replace("ab","AB"))   # Заменить на AB
print(msg.replace("ab",""))     # Заменить на ничего - удалить
print(msg.replace("a","o",2))   # Меняем только 2 параметра

# Если строка состоит из букв, НО если есть пробел то false
msg ='abra'

print(msg.isalpha(),"Да буквы") # Состоит ли из буквенных
msg ='abra cadabra'
print(msg.isalpha(),"Есть пробелы")
msg =msg.replace(" ","")
print(msg.isalpha(),"Убрали пробелы  и тут теперь только буквы")

# Если строка состоит из цифр (2.0 вещественные не сработает) не один символ
msg = "12345"
print(msg.isdigit())
d ="abc"
# Заполнитель отступатель
print(d.rjust(5))       # Подставляет пробелы
print(d.rjust(6,'0'))   # Подставляет 0
print(d.rjust(6,'0'))   # Подставляет 0
print(d.ljust(10,"*"))

# Уберем все лишние пробелы Првевращает в строку

d ="1,2  ,3  , 4, 5,6,  7"
print(d)
d=d.replace(" ","")
print(d.split(","))

# ИЗ СПИСКА строк !!! Првевращает в строку
msg =["Привет","МИША"]
print(msg)
print(" ".join(msg))

# Удаляет пробелы слева и справа
msg= "   Hello world   "
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())