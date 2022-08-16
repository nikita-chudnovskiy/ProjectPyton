file = open(r'file.txt',encoding='utf-8')

s=file.readlines()
print(s)

khutor =[]

for i in range(len(s)):
       print(s[i])
       if s[i]=='tcs1111\n':
              khutor.append(s[i])
print(khutor)













