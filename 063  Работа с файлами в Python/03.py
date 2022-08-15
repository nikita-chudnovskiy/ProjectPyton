file = open(r'TCS.txt','a+',encoding='utf-8')
file.seek(0)
file.write('tcs111\n')
file.seek(0)
print(file.read())
file.seek(0)


for row in file:
    print(row)

file.close()