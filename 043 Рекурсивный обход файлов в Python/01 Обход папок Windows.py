import os
#os.isdir
#os.isfile

#path =input('Ведите путь где искать ')
path = 'C:\\Movies'   # Путь где искать

print(os.listdir(path)) # os.listdir показывает содержимое по указанному пути в виде списка

name = '123'
for i in os.listdir(path): # функция возвр все в виде списка

    print(path+'\\'+i,os.path.isdir(path+'\\'+i)) # папки файлами не являются






# print('Нажмите 1 для выхода')
#
#
# while True:
#     a = int(input())
#     if a ==1:
#         print('Exit')
#         break
#     else:
#         print('Нажмите 1 для выхода')
# else:
#     print('Завершено')
