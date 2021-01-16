password = 'qwerty'

print(password[0:])    # qwerty
print(password[0:3])   # qwe      0,1,2  до третьего индекса
print(password[:])     # qwerty
print(password[0:5:2]) # qet  шаг через 1
print(password[-1])    # y  последний
print(password[:-1])   # до предпоследнего
print(password[2:-1])





password=password[-1]+'nnn'+password
print(password)