# Генератор словаерей


a =[i*i for i in range(1,11)]
print(a)


# i ключ i**i его значение

a ={i:i**2 for i in range(1,11)}
print(a)



# key : value ( ключем будет слово а значением длинна)
a ={world:len(world) for world in ['barboriska','world','www']}
print(a)


data = {
    'ДжеФФ БезоСС': '177',
    'ИЛоН Маск': '126',
    'Билл ГЕЙТС': '110'
}

print()
# Ключ с большой буквы , значения int  (data.items возвр сразу ключ и значение)
new_data = {key.title(): int(value)for key,value in data.items()}

print(data)
print(new_data)


print()
users = [
    [0,'Bob','password'],
    [1,'code','python'],
    [51,'Stack','overflow']
]

new_users ={users[0]:users for users in users} # Превращаем в словарь
print(users[2]) # в таком случае по ключу нельзя обращатся
print(new_users[51])

