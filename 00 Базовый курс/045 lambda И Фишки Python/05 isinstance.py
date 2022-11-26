a = [2,3,[3],'hi','all',[5]]
stroka = ''
s_list =[]
numbers=0
for i in a:
    if isinstance(i,str):
        stroka+=i
    elif isinstance(i,list):
        s_list=s_list+i
    elif isinstance(i,int):
        numbers=numbers+i
print(stroka)
print(s_list)
print(numbers)



# Проверка на тип
z= 10
print(isinstance(z,int))