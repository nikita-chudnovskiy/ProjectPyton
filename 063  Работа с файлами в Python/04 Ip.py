import os
import socket
import ipaddress
print('******* Tinkoff Ploshadka IP Sutup Tools v.2 *********')
import getpass

ipUP=[]
ipDown=[]

with open(r'C:\My Python\ProjectPyton\063  Работа с файлами в Python\file.txt',encoding='utf-8') as file:
    s =file.read().splitlines()
    print(s) # Наш список пк
    khutor = 'Khutor'

    for i in range(len(s)):  # пройтись по всей длинне списка
        name =s[i] # переменной name присваисваем имена машин

        poteri=os.system("ping -n 1  " + name) # poteri переменная для если 0 то выполнится пингует пк


        if poteri == 0:
            IP_addres = socket.gethostbyname(name) # создали переменную IP_address проходится по нашему списку

            addr4 = ipaddress.ip_address(IP_addres) # addr4 показывает ip
            if addr4 in ipaddress.ip_network('192.168.1.0/24'): # Если наш ip попадает в подсеть то добовляется в список IpUP
                ipUP.append(f"{name} {IP_addres} {khutor} ")

        else:
            #print(name, 'is down!')
            ipDown.append(name) # Отрабатывает else то сюда улетают пк down



with open(r"C:\Up.txt", "w") as file:
    print(*ipUP , file=file,sep='\n')

# with open(r"C:\Down.txt", "w") as file:
#     print(*ipDown, 'Vodniy', file=file,sep='\n')
#
#
# file.close()




