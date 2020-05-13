a =[1,2,3]
while len(a)>0:
     print(a[0])

     if a[0] >2:
          print('больше')
     elif a[0]==2:
          print('равно')
     else:
          print('меньше ')
     a=a[1:]

