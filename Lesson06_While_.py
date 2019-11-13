x = int(input())
while x <= 10:         # Чтобы прервать цикл while досрочно исп инструкцию break
	print(x)
	x += 1
	if x > 5:
		print('Print Breaking')
		break
print('Finish')
