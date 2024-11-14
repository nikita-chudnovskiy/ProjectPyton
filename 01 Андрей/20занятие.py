b = []
h = []
for i in range(5):
    a = input()
    b.append(a)
for i in range(5):
    c = input()
    h.append(c)
for i in b:
    if i not in h:
        print(i)
