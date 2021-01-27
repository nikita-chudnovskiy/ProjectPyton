text = input()
a = set()
while text !='':
    slova = text.split()
    a.update(slova)
    text = input()
    print(a)
print(len(a))