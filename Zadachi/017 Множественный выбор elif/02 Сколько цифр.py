# Сколько в числе цифр

a = int(input())
if a<0 or a >10000:
    print('error')
elif a<10:
    if a%2==0:
        print('1 digit chet')  # Также добавлена проверка на четность !
    else:
        print('1 digit nech')
elif a < 100:
    print('2 digit')
elif a < 1000:
    print('3 digit')
elif a < 10000:
    print('4 digit')