list1 = [1, 3, 3, 3, 3, 3, 4, 9]
list2 = [2, 2, 2, 2, 4, 4, 4,11]

# Объединение Списков применив множества
list3 = (set(list1) | set(list2))
print(type(list3),list3)


a =['Июнь','Июнь','Июль','Август']
b = ['Июнь','Август']

print(set(a)) # Множество хранит только уникальные
print(set(a)&set(b)) # Пересечение списков Июнь Август
