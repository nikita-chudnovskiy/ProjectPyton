n = [2,3,2]
b=[]
for i in range(len(n)):
    if i not in b:
        b.append(i+1)
        print('Yes')
    else:
        print('No')
print(b)
