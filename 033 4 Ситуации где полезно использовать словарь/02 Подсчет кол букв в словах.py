example = input()

count = {}

for i in example.split():
    count[i] = len(i)

print(count)


