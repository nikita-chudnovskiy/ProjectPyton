password = 'qwerty'

print(password[0:])    # qwerty  начни с 0 и до конца
print(password[0:3])   # qwe 0,1,2  до третьего индекса
print(password[:])     # qwerty вся строка
print(password[0:5:2]) # qet шаг через 1
print(password[-1])    # y  последний
print(password[:-1])   # до предпоследнего
print(password[2:-1])

#  ----------------------
#  | H | e | l | p | A |
#  ----------------------
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1

password=password[-1]+'nnn'+password
print(password)
