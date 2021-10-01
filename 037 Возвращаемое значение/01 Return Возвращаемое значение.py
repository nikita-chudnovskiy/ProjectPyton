# Любая фенкция если не указано возвращает значение None

def sAndPerim(a,b):
    return a*b,2*(a+b)

a =sAndPerim(2,5)

print(a)


# Дали имена
square,perim =sAndPerim(2,5)
print(square,perim)

# Возвращать можем любое значение

def sqAndPer(a,b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas
print(sqAndPer(2,4))