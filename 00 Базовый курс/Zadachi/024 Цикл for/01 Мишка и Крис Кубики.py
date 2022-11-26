from random import randint
sm =0
ss=0
n =int(input())
for i in range(n):
    mishka =randint(1,6)
    cris = randint(1,6)
    sm+=mishka
    ss+=cris
    print('Кубики Мишки',mishka,end='  ')
    print('Кубики Криса',cris)
print()
print('Числа мишки',sm)
print('Числа Крис',ss)
if sm>ss:
    print('Мишка победил')
elif sm<ss:
    print('Крис победил')
else:
    print('Ничья')



#    if sm>ss:
#        print('Мишка')
#    elif sm<ss:
#        print('Silver')
#    else:
#        print('Frendship..........')
