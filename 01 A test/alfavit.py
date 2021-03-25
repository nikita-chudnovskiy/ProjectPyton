a=ord('а') # Перевод в числа unicod русском

for i in range(32):
    print(chr(a),end= ' ') # Перевод в символы
    a+=1

print()

a = ord('a')

while a <=ord('z'):
    print(chr(a),end= ' ')
    a+=1


