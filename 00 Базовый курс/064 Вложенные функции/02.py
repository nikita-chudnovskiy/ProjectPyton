#Пример 1
y = 2
def main_func(x):
    return y*x     # использует глобальную

print(main_func(8))


z = 2
# Локальные Переменные будут удалятся после вызова каждый раз
def degree(x):
    z =10      # Используется локальная переменная
    return z*x
print(degree(8))



def degree(x):
    z =10
    def degree_twho():
        return z*x
    return degree_twho()

print(degree(100))