# Делители Числа 20 , когда это число делится без остатка

# n
# 20  [1],2,4,5,[20]   наименьший делитель числа [1], наибольший [20]
# 6   [1],2,3,[6]


n = int(input('введите число'))
i =1
while i<=n:  # i<=n//2  В 2 РАЗА БЫСТРЕЕ
    if n%i==0:#  выводим все числа без остатка
        print(i,end=' ') # отменили перенос
    i+=1

