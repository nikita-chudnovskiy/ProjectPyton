def aaa():
    return [43,35,22]

print(aaa())



def genf():

    for i in [43,22,33]:
        yield  i

s =genf()

print(next(s))
print(next(s))
print(next(s))


print('следующий')




def genG():
    s=7
    for i in [43,22,33]:
        yield  i              # Она Возвращает значение и замораживает вашу фунуию со всеми локальными переменными на этом месте
        print(s)
        s =s*10+7

g =genG()
print(next(g))
print(next(g))
print(next(g))
print(next(g))