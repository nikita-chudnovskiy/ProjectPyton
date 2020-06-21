for i in range(3):
    print('inside', i)
    print('hello')

print('Outside',i) # последнее число


for i in range(50):
    if i%2==0 and i%7==0: # Числа делятся на 2 и на 7
        print(i)

# Квадрат числа
print()
for i in range(7):     # квадрат числа i
        print(i,i**2)


# сумма всех двухзначн чисел
s =0
for i in range(10,100):
    s =s+i
print(s)


# factorial 5 пяти     1*2*3*4*5
pr =1
for i in range(1,6):
    pr = pr *i
print(pr)


n=int(input())   #  factorial тот что вводим    т+1 потомучто если мы хотим факториал 5 то введем 5 +1 (1*2*3*4*5)
pr =1
for i in range(1,n+1):
    pr = pr *i
print(pr)

# Обходили заданную последовательность !!!