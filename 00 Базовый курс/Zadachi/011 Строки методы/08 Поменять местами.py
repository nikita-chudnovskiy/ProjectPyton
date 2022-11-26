a = 'Hello World'
print(len(a.split())) # Сколько слов
print(a.find(' ')) # Ищем прбел
a=a[6:]+' '+a[0:6] # берем срезы
print(a)


str = "hello world"
str =" ".join(str.split()[::-1]) # Вначале применяем что становится списком , потом применяется смена местами через срез перевернуть
print(str)

# Наглядный пример !!!
a = ['hhh','www']
print(a[::-1])