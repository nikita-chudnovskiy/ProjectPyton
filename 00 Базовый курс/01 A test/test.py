# put your python code here


# s = ["Уфа", "Астрахань", "Москва", "Самара" ,"Казань"]
# s1 =[i for i in s if i !="Москва"]
# print(*s1)
#
#
# a = input().split()
# if 'Москва' in a:
#     a.remove('Москва')
# print(*a)

#
# a,b,c,d = map(int,input().split())
# if a-2>=c and b-2>=d or  a-2>=d and b-2>=c:
#     print('ДА')
# else:
#     print('НЕТ')

# number =int(input())
# a =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# for i in range(len(a)):
#     if number == i:
#         print(a[i])


# m =int(input())
# if m ==1 or m ==3 or m==5 or m==7 or m==8 or m ==10 or m ==12:
#     print(31)
# elif m ==2:
#     print(28)
# elif m ==4 or m ==6 or m ==9 or m == 11:
#     print(30)


a = int(input())
m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
m28 = [2]
if a in m31:
    print(31)
elif a in m30:
    print(30)
elif a in m28:
    print(28)
else:
    print("Улыбка")