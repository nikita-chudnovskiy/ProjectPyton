file = open(r'TCS.txt',encoding='utf-8')

s =file.readlines() # Сделать списком
print(s)

for i in range(len(s)):
    print(i,s[i],end='')


