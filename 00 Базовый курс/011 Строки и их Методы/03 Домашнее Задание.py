# Вывести первую заглавную
a ="HELLO"
print(a.capitalize())

# Найти число вхождений
# Привет-Мир-МОЙ
s= "Привет-Мир-МОЙ"
print(s.count("-"))
# index, если указанный фрагмент не будет найден в строке? Ошибка
# String.find, если указанный фрагмент не будет найден в строке? -1

# Найти индекс первого вхожления abrakadabra
s ="abrakadabra"
print(s.find("ra"))



# dobavlyaem---slagi--slug-k--url---adresam
s="dobavlyaem---slagi--slug-k--url---adresam"
s =s.replace("---","--")
s=s.replace("--","-")
print(s)


# Вывести в столбик 008 011 123
a,b,c=8,11,123
a =str(a)
b =str(b)
print(a.rjust(3,"0"),b.rjust(3,"0"),c,sep="\n")

# Сколько слов
a="I LOve YOU".split()
print(len(a))

# Заменить
s="Москва Тверь Казань"
print(s.replace(" ",";"))



"""
String.rjust
String.ljust
String.strip
String.rstrip
String.lstrip
String.rfind
Расширяет строку, добавляя символы слева
Расширяет строку, добавляя символы справа
Удаляет пробелы и переносы строк справа и слева
Удаляет пробелы и переносы строк справа
Удаляет пробелы и переносы строк слева
Возвращает индекс первого найденного вхождения при поиске справа
"""