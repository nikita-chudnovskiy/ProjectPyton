# Аргумент key в сортировке
# 1) Встроенная функция
# 2) Передавать собственную функцию
# 3) Встроенные методы обьектов
# 4) Анонимные функции lambda
#1 Способ
a =[4,-6,5,99,8,9,-5]
print(sorted(a))
print(sorted(a, key=abs))

#2 Способ
# Своя функция , возвращает посл цифру этого числа
def f(x):
    return x%10

print('*********')

print(sorted(a,key=f))



#3 Способ
a =['ZZZ','aaa','eeee','DDD','BBB','wwww']

print(sorted(a))
print(sorted(a,key=str.lower))


# 4 Способ

a =['ZZZ 800','aaa 45','eeee 43','DDD 800','BBB 43','wwww 14']

print(sorted(a,key=lambda x: (int(x.split()[1]), x.split()[0].lower())))