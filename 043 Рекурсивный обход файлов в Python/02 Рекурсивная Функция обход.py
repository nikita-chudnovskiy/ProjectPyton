import os

path = 'C:\\Movies'
#path =input('Ведите путь где искать ')
#name =input('Что ищем')
def obxodFiles (path,level=1,name ='123'):
    print(os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Спускаемся',path+'\\'+i)
            obxodFiles(path+'\\'+i,level+1)
            print('Возвращаемся',path)
#obxodFiles(path)



def obxodF (path,level=1,name ='123.txt'):

    for i in os.listdir(path):
        if (i == name):
            print(path + '\\' + i,level)
        if os.path.isdir(path + '\\' + i):
            obxodF(path+'\\'+i,level+1)
obxodF(path)


print('Нажмите 1 для выхода')
while True:
    a = int(input())
    if a ==1:
        print('Exit')
        break
    else:
         print('Нажмите 1 для выхода')
else:
    print('Завершено')
