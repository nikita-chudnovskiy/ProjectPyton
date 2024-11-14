# x = 50
# def zzz(x):
#     print(x)
#     x =2
#     print('замена локального х на',x )
# zzz(x)
# print(x,'по прежнему')
# print()
#
# x = 50
# def zzz():
#     global x
#     print('x равно',x )
#     x =2
#     print('замена локального х на',x )
# zzz()
# print(x,'Поменялось')
#
# print()

def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()
print()

