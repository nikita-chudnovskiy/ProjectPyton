# print(59%10)
# print(59//10)

first = int(input())
second = int(input())

f3 = first % 10
first = first // 10
f2 = first % 10
first = first // 10
f1 = first % 10

s3 = second % 10
second = second // 10
s2 = second % 10
second = second // 10
s1 = second % 10

print(f'{(f1 + s1) % 10}{(f2 + s2) % 10}{(f3 + s3) % 10}')