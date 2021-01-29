person = {}

s = 'IVANOV IVAN  SAMARA SGU 5 4 5 4 3'
s = s.split()

# Создаем ключи
person['LastName'] = s[0]
person['Name'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(person)

