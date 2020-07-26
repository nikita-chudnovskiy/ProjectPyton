a =[1,'b','c','b']
b =a.copy()
for i in range(len(a)):
    if 1 in b:
        b.remove(1)
    if 'b' in b:
        b.remove('b')
print(a)
print(b)