b = None
for i in range(5):
    a = int(input())
    if b == None:
        b = a
    if b != None:
        if b < a:
            b = a
print(b)