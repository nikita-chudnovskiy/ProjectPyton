# Деление нацело и деление по остатку
# Давайте начнем с деления нацело. В Python данная операция обозначается знаком двойного слеша //.

# "Cколько раз второе число  умещается в первое?"
print(21//5)
print(37//10)
print(42//6)
print(5//8)
print(17956//1000)
print(37//8)

# Остаток от деления
#"Сколько останется от первого числа после того, как в него максимальное количество раз уместится второе число?"
print(31%5,'31 %5 Остаток от деления')
print(89%10,'89 %10 Остаток от деления')
print(35%7)
print(5%13)
print(8541%100)
print(37%8)

# //
print(1234//10,'Убирается 1 посл цифра')     # Убирается 1 посл цифра
print(1234//100)    # Убирается 2 посл цифры
print(1234//1000)   # Убирается 3 посл цифры
# %
print(1234%10,'Останется последняя')
print(1234%100,'Останется 2 последнии')
print(1234%1000,'Останется 3 последнии')

# Разложение числа
x = 12345
a = x//10000     # убираются посл 4 цифры Остается ПЕРВАЯ
b = x//1000%10   # убираются посл 3 цифры и остаток посл цифра
c = x//100%10    # убираются посл 2 цифры и ост посл число
d= x//10%10      # убираются посл 1 цифра
e= x%10         # на 10 остаток посл цифра

print(a,b,c,d,e,sep='')

# Отдельно посмотреть эту тему
# -11 % 10
# 11 % -10
# -11% -10
