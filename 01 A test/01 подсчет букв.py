b = input()

slovar = {}

for i in b:
    if i in slovar:
        slovar[i] += i
    else:
        slovar[i] = 1
print(slovar)
