b =input()

slovar={}

for i in b:
    if i in slovar:
        slovar[i]+=1
    else:
        slovar[i]=1
print(slovar)