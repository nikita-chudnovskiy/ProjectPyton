file = open(r'TCS.txt',encoding='utf-8')

s =file.readlines()
print(s)

for i in s:
    print(i,end='')


