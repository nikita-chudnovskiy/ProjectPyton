file = open('Брат2.txt','a+',encoding='utf-8') # r -чтение w -запись  a - допишется в в конец, a+ чтение и запись
#s= file.readlines()  Поместить в список
#print(s)
file.write('AAAAAAAA\n')
file.write('AAAAAAAA\n')
file.seek(0)


