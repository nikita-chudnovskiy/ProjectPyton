m28=[2]
m31=[1,3,5,7,8,10,12]
m30 =[4,6,9,11]
t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, num = map(int, input().split())
if m in m28 and num <= 28 and m<=12 and num <=31:

    if num ==28:
        m = str(m)

        num0 = int(num) - 1
        num0 = str(num0)

        num = 1
        num = str(num)

        m1 = int(m) + 1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))
    elif m in m28 and num <=27 and num >=2:
        m = str(m)

        num0 = int(num) - 1
        num0 = str(num0)

        num = num +1
        num = str(num)

        m1 = int(m)
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))

    elif num == 1:
        m = 1
        m = str(m)

        num0 = 31
        num0 = str(num0)

        num = num+1
        num = str(num)

        m1 = int(m)+1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))


############################################################

elif m in m31 and num <= 31:
    if num ==31:
        m = str(m)

        num0 = int(num) - 1
        num0 = str(num0)

        num = 1
        num = str(num)

        m1 = int(m) + 1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))

    elif m in m31 and num <=30 and num >=2:

        m = str(m)

        num0 = int(num) -1
        num0 = str(num0)

        num = int(num)+1
        num = str(num)

        m1 = int(m)
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))


    elif m in m31 and m ==1 and num ==1:
        m  = 12
        m = str(m)

        num0 = 31
        num0 = str(num0)

        num = int(num)+1
        num = str(num)

        m1 = 1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))




elif m in m30 and num <=30:
    if num ==30:
        m = str(m)

        num0 = int(num) - 1
        num0 = str(num0)

        num = 1
        num = str(num)

        m1 = int(m) + 1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))

    elif m in m30 and num <=30 and num >=2:

        m = str(m)

        num0 = int(num) -1
        num0 = str(num0)

        num = int(num)+1
        num = str(num)

        m1 = int(m)
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))


    elif m in m30 and  num ==1:
        m  =int(m)-1
        m = str(m)

        num0 = 31
        num0 = str(num0)

        num = int(num)+1
        num = str(num)

        m1 = int(m)+1
        m1 = str(m1)

        print(m.rjust(2, '0') + f"." + num0.rjust(2, "0"), m1.rjust(2, '0') + f"." + num.rjust(2, '0'))

else:
    print("Вводите верно дату")
    print(f'{m - 1:02}.{t[m - 2]:02} {m:02}.{num:02}')