def f (x):
    return x>9 and x <100 # x%2==0

a =[1,5,12,3,2,5,1,10,11,0,65,111]

b = list(filter(f,a))
print(b)

# Можно и генератором обойти
b = [i for i in a if i>9 and i<100]
print(b)

a =[1,5,12,3,2,5,1,10,11,0,65,1110,0,'hi','all',''] # Пустое значение не возьмет


b = list(filter(bool,a)) # Функции 0 значения не возьмет
print(b)


# Можно применять lyamda слово больше 4 букв
a =['hi ','all','Hello']
b =list(filter(lambda x:len(x)>4,a))
print(b)


a ='sdfsf4234sdfdsf'
b =list(filter(str.isdigit,a)) 
print(b)