file = open('Брат2.txt','a+',encoding='utf-8') # r -чтение w -запись  a - допишется в в конец, a+ чтение и запись
#s= file.readlines()  Поместить в список
#print(s)
print(file.read())

file.write('hello\n')
print(file.read())
print(file.seek(0))
print(file.read())


