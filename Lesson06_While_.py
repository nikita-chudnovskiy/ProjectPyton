x = int(input())
while x <= 10:  # Чтобы прервать цикл while досрочно исп инструкцию break
    print(x)
    x += 1
    if x >= 10:
        print("Вышли из цикла")#
        break
else:
    print('Finish')
