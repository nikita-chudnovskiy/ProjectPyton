# Наибольшие числа 🌶️🌶️

max1 = 0
max2 = 0
n = int(input())
for _ in range(1, n + 1):  # n>2˚
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        ma2 = num
print(max1, max2, sep='\n')

# print(*sorted(int(input()) for i in range(int(input())))[-2:][::-1], sep='\n')

# z =[int(input()) for i in range(int(input()))]
# print(sorted(z)[-1],z[-2])
