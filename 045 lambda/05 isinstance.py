a = [2,3,'hi','all',5]
stroka =''
s =0
for i in a:
    if isinstance(i,str):
        stroka+=i
    else:
        s+=i
print(stroka,s)



# Проверка на тип
z= 10
print(isinstance(z,int))