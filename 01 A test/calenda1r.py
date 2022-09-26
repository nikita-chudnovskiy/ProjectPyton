import calendar

god =int(input('Введите год !'))
print()
c=calendar.TextCalendar()
print(c.formatyear(god))

file =open(r'C:\My Python\ProjectPyton\01 A test\calendar.txt','a+',encoding ='utf-8')
print(file.read())
file.write(c.formatyear(god))
a=int(input())
