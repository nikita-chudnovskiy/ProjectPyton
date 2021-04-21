my_box ={'слон':'элефант',2:'2'}
print(my_box)

my_box[3]='three'
print(my_box)

# set Нам просто добавит если нет Мурзика
print(my_box.get('kot','Мурзик'))
print(my_box)

# setdefault добавит в словарь ключ кот и Мурзик
my_box.setdefault('Кот','Мурзик')
print(my_box.items())
