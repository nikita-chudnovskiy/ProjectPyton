# # Найти все индексы ра


s=input()
if not 'ра' in s:
    print(-1)
else:
    for i in range(len(s)-1):
        if s[i]=='р' and s[i+1]=='а':
            print(i,end=' ')


# Вводится строка с номером телефона. Ожидается формат ввода:
# +7(xxx)xxx-xx-xx
s=input()

flag =False

for i in range(len(s)):
    if s[0]=='+' and s[1]=='7'\
        and s[2]=='(' and  s[3:5].isdigit() and s[6]==')' \
        and s[7:9].isdigit() and s[10]=='-' and s[11:12].isdigit()\
        and s[13]=='-' and s[14:15].isdigit() and len(s)==16:

        flag =True
    else:
        flag= False
if flag:
    print("ДА")
else:
    print("НЕТ")
# Большой подвиг 3. В виде строки записано арифметическое выражение, например:
#
# "10 + 25 - 12"
#
# или
#
# "10 + 25 - 12 + 20 - 1 + 3"
#
# и т. д. То есть, количество действий может быть разным.
p = input().replace(' ', '').replace('+', ' + ').replace('-', ' - ').split()
s = int(p[0])
for i, b in enumerate(p):

    if b == '+':
        s += int(p[i + 1])

    if b == '-':
        s -= int(p[i + 1])
print(s)

# каждое значение этого списка изменить, возведя в квадрат.
# Sample Input:
#
# 8 -11 4 3 6
# Sample Output:
#
# 64 121 16 9 36
s =list(map(int,input().split()))
for i in s:
    print(i*i,end=" ")

# Sample Input:
#
# 8 11 2
# Sample Output:
#
# 8 8 11 11 2 2
lst = list(map(int, input().split()))
for i, value in enumerate(lst):
    print(lst[i], value, end=' ')

# Минимальное в списке
lst = list(map(float, input().split()))
a = lst[0]
for i in lst:
  if i < a:
    a = i
print(a)

# Sample Input:
#
# -5.67 3.5 6.89 -3.0
# Sample Output:
#
# -1.0 3.5 6.89 -1.0

lst = list(map(float, input().split()))
for i, n in enumerate(lst):
    if lst[i]<0:
        lst[i] = -1.0
    print(lst[i],end=' ')