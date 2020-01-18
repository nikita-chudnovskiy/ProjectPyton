k =int(input())
a = [1,5,10,20,100]
b1=k%100
a1=k//a[4]
if k >100:
    print(a1 =k//a[4])
    print(b1 = k%100)

elif k<=20:
    a2 =b1//a[3]
    b2 =k%100

a3 = b2//a[1]
b3 = k%100
print(a1,a2,a3)
l = [a1,a2,a3]
print(len(l))