def s():
    a = 11
    b = 22
    global c # поменяли глобальную переменную
    c = 33 # если закоментируем то возьмет значение из Global
    print(a,b,c,'local')



#global
a =100
b =200
c =300

s()
print(a,b,c,'global')