# Пузырьковая сортировка -сравнение начинаем с крайхних элементов , если елемент меньше то меняем местами
# и так далее пока в конце не всплывет наш пузырек и число не окажется максимальным
# И так несколько проходов пока не всплывут все пузырьки.

n = int(input()) # 5 7 4 3 8 2
count =0
mas = list(map(int,input().split()))
for run in range(n-1):
    for i in range(n-1-run):
        if mas[i]>mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1],mas[i]
print(mas)
print(count, 'прохода')
