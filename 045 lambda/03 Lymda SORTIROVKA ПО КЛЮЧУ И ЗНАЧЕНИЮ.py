a ={'Я робот':88,
    'Робот А':77,
    'Асупер Робот':23,
    'Крохотный робот':24,
    'Маленький робот': 24,
    'A ппп':23
    }

for i in sorted(a.items(),key=lambda para: (para[1],para[0])):
    print(i)

