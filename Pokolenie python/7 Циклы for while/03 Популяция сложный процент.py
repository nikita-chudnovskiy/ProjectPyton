# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.


m = float(input())
p = float(input())
n = int(input())

for i in range(n):

    print(i+1,(m*(1+p/100)**(i))) # Решается по формуле сложный процент  m 100000 p 1%  n кол дней