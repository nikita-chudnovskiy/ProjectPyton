import locale
import datetime
data = datetime.datetime.today()
print(data)



locale.setlocale(locale.LC_ALL, "ru") # задаем локаль для вывода даты на русском языке

today = datetime.datetime.today().strftime("%A, %c") #
print(today)
