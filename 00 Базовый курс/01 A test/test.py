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

t=float(input())
print("green" if (60 - t)%5 > 2 else "red")