

#наибольшее значение присвоить переменной d и вывести ее на экран.
a=float(input())
b=float(input())
print( a if a>b else b)




#Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3"
a =int(input())
print( "кратно 3" if a%3==0 else "не кратно 3")


# Палидром
msg =(input()).lower()
print("палиндром" if msg[::-1]==msg else "не палиндром")


#Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True".

a =int(input())
d ="False" if a==0 else "True"
print(d)


#  в диапазоне [0; 59]. Если значение равно 59, то следующее должно быть 0
n = int(input())
res = 0 if n + 1 == 60 else n + 1
print(res)


# до и фа дополнительно ставить символ диеза '#'.
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
notes = list(map(int, input().split()))
for i in notes:
    print('#'+m[i-1] if m[i-1] == "до" or m[i-1] == "фа" else m[i-1], end = ' ')