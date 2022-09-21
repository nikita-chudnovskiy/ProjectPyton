import os
import socket
import ipaddress
print('******* Tinkoff Ploshadka IP Sutup Tools v.2 *********')
import getpass

ipUP=[]
ipDown=[]
print('Укажите путь к вашему файлу с Пк: ')
#way =input()
with open(r'C:\namePC.txt',encoding='utf-8') as file:
    s =file.read().splitlines()
    print(s) # Наш список пк

    for i in range(len(s)):  # пройтись по всей длинне списка
        name =s[i] # переменной name присваисваем имена машин

        poteri=os.system("ping -n 1  " + name) # poteri переменная для если 0 то выполнится пингует пк
        khutor ='Khutor'
        vodniy ='Vodniy'
        g =' ' # для удобства разделить ip от имени
        if poteri == 0:
            IP_addres = socket.gethostbyname(name) # создали переменную IP_address проходится по нашему списку
            user = getpass.getuser()
            print("Host Name is:" + name)
            print(name, "Computer IP Address is:" + IP_addres)
            print(user)
            addr4 = ipaddress.ip_address(IP_addres) # addr4 показывает ip
            if addr4 in ipaddress.ip_network('192.168.2.0/24'): # Если наш ip попадает в подсеть то добовляется в список IpUP

                ipUP.append(name+g+IP_addres+g+khutor+g+user)
            elif addr4 in ipaddress.ip_network('192.168.1.0/24'):
                ipUP.append(name+g+IP_addres+g+vodniy+g+user)

        else:
            #print(name, 'is down!')
            ipDown.append(name) # Отрабатывает else то сюда улетают пк down
print(ipUP,'ip up')
print(ipDown,'ip down')


with open(r"C:\Up.txt", "w") as file:
    print(*ipUP,  file=file,sep='\n')

with open(r"C:\Down.txt", "w") as file:
    print(*ipDown, file=file,sep='\n')

a=int(input())

file.close()




