example = input()

count = {}
g=0
for i in example.split():
    count[i] = len(i)
    g =g+1
print(count,g)


