
# Методы строк
# S.capitalize()                Заглавная
# S.upper()                     все большие
# s.lower()                     все маленькие

# s.count('e',1,9])             Что ищем i  с как по какую Сколько раз встретится
# s.find(sub[, start[, end]])   Что ищем  i Поиск Индекс Буквы i самый маленький- первый индекс(если нет возвр -1)
# s.rfind('e'))                 Ищем индекс с права на лево
# s.index('e'))                 разница между find и index Если нет то возвр ошибку а метод find -1

# s.replace('h','???',1))       Что будем менять на что будем менять, сколько замен a.replace('i','a',1) 'Nakita'

# s.isalpha()                   Cостоит из букв если да то True если есть пробел false
# s.isdigit()                   Проверяет из цифр ли строка

# s.rjust(10,'0')               Сдвигаем вправо на какое хотим   xxx123 колич (10,вмето пустого места ставим 'xxx'
# s.ljust(10,'0')               меняем значение с лева на право  123xxx


d = 'Hello World'
# print(d.split())            # Данный метод разбивает строку по пробелу и превращает в список из трех строк
# ['Привет', 'Иван', 'Петрович']

#print(len(d.split()))  Емли хотим узнать сколько слов в нашей строке !!!!
print(d.split('o'))         # Разбить строку по букве n

w = '23, 24, 45, 47'.split(',') # разбить список запятой
print(w)
print(' ='.join(w))          # разделить список через =
print('.'.join(d.split()))  # разделить список через .
print(','.join(d).split())  # разделить каждый элемент через ,

a ='Hello   '
b = '   12'
c = 'abcd    '
print(a.rstrip())   # метод удаляет пробелы и перенос на новые строки
print(b.lstrip()) # удаляет слева
print(c.strip())  # удаляет справа

a = input().replace('e','k').upper() # заменить e на k методы можно вызывать цепочками
print(a)


"""
Функция или метод	Назначение
S = 'str'; S = "str"; S = '''str'''; S = str	Литералы строк
S = "s\np\ta\nbbb"	                            Экранированные последовательности
S = r"C:\temp\new"	                            Неформатированные строки (подавляют экранирование)
S = b"byte"	                                    Строка байтов
S1 + S2	                                        Конкатенация (сложение строк)
S1 * 3	                                        Повторение строки
S[i]	                                        Обращение по индексу
S[i:j:step]	                                    Извлечение среза
len(S)	                                        Длина строки
S.find(str, [start],[end])	                    Поиск подстроки в строке. Возвращает номер первого вхождения или -1
S.rfind(str, [start],[end])                   	Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
S.index(str, [start],[end])	                    Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
S.rindex(str, [start],[end])	                Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
S.replace(шаблон, замена)	                    Замена шаблона
S.split(символ)	                                Разбиение строки по разделителю
S.isdigit()	                                    Состоит ли строка из цифр
S.isalpha()	                                    Состоит ли строка из букв
S.isalnum()	                                    Состоит ли строка из цифр или букв
S.islower()	                                    Состоит ли строка из символов в нижнем регистре
S.isupper()	                                    Состоит ли строка из символов в верхнем регистре
S.isspace()	                                    Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
S.istitle()	                                    Начинаются ли слова в строке с заглавной буквы
S.upper()	                                    Преобразование строки к верхнему регистру
S.lower()	                                    Преобразование строки к нижнему регистру
S.startswith(str)	                            Начинается ли строка S с шаблона str
S.endswith(str)	                                Заканчивается ли строка S шаблоном str
S.join(список)	                                Сборка строки из списка с разделителем S
ord(символ)	                                    Символ в его код ASCII
chr(число)	                                    Код ASCII в символ
S.capitalize()	                                Переводит первый символ строки в верхний регистр, а все остальные в нижний
S.center(width, [fill])	                        Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
S.count(str, [start],[end])	                    Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
S.expandtabs([tabsize])	                        Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам
S.lstrip([chars])	                            Удаление пробельных символов в начале строки
S.rstrip([chars])	                            Удаление пробельных символов в конце строки
S.strip([chars])	                            Удаление пробельных символов в начале и в конце строки
S.partition(шаблон)	                            Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
S.rpartition(sep)	                            Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку
S.swapcase()	                                Переводит символы нижнего регистра в верхний, а верхнего – в нижний
S.title()	                                    Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
S.zfill(width)	                                Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями
S.ljust(width, fillchar=" ")	                Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar
S.rjust(width, fillchar=" ")	                Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar
S.format(*args, **kwargs)	                    Форматирование строки
"""

