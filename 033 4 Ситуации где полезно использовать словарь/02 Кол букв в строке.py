s = input()
d = {}
for i in s:
    if i.isalpha():
        d[i]=d.get(i,0)+1

for i in sorted(d):
    print(i,d[i])
