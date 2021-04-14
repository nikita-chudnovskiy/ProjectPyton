person ={}

s =' Ivanov Ivan Samara 5 4 3'
s =s.split()

# Создали ключи и присвоили им значения строки 0 1 2 , далее три значения закинули в 4 ключ Оценки
person['lastName'] =s[0]
person['firstName'] =s[1]
person['City'] =s[2]
person['Ocenki']=[]   # создали пустой список

for i in s[3:]: # в 4 элемент оценки
    person['Ocenki'].append(int(i))
print(s)
print(person)
