a: int = 100
print(a)


a: int = 100
a='100' # тут мы список ввели а должны int
print(a)



def antonaciya(a,b):
    return a+b

print(antonaciya(2,3))





def antonaciya(a: int,b:int | float | str ):
    return a+b

print(antonaciya(1,'2'))
