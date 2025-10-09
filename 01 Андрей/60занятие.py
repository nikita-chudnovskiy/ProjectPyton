def RichardDucky(text):
    j = []
    for i in text.split():
        if i[-3:] == 'тся':
            j.append(i)
    return(j)
f = open('kd.txt',encoding='utf-8')
r = f.read()
f.close()

k = RichardDucky(r)
print(k)