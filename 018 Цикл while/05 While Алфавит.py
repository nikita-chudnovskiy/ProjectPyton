lenguage=input('выберите язык ru или angl ')

while lenguage != 'angl' and lenguage !='ru':
    print('не правильный выбор')
    lenguage =input('Введите еще раз')
    continue
if lenguage =='angl':
    a = 'a'
    i = 0
    while i <=25:
        print(a,end=' ')
        a=chr(ord(a)+1)
        i+=1
elif lenguage =='ru':
        a = 'а'
        i = 0
        while i <= 33:
            print(a, end=' ')
            a = chr(ord(a) + 1)
            i += 1

print()

test =[]
alfa = 'a'
i=0

while i <=25:
    test.append(alfa)
    alfa =chr(ord(alfa)+1)
    i+=1
#   print(test) будет добавлять и выводить по 1 букве
print(test) # Вывод уже заполненного списка


# Способ без списка и (со списком раскоментировать)
#t1 =[]
import string
for a in string.ascii_lowercase:
    print(a, end = ' ')
    #t1.append(a)
#print(t1)