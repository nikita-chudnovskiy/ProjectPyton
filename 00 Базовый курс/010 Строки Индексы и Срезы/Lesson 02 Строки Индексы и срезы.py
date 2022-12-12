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

a = 'oajdoiajdioajfdioajfij'
print(len(a))  # длинна

s ="Balakirev"
print(s[-3:])  # Последние 3
print(s[0:4])  # 0 до 4
print(s[0]+s[-1]) #1 и посл
print(s[1::2]) # c 2 и через 1


s ="Hello"
s1 ="Python"
print(s[0::2],end=" ")
print(s1[1::2])

s = "abrakadabra"
s= s[0:5]
print(s[::-1])



s ="Hello"

s1 ="Balakirev"
print(len(s))
print(s1[0:5],end=" ")

print(s1[0:len(s)])

