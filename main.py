#import package1
#from package1 import file2 # Теперь не нужно писать  package2.file2.a
#from package1.file2 import c  # Обращаемся уже напрямую

#print(package1.file1.d)
#print(file2.a)

#package1.a # уже нет доступа к переменной d !!!
#package1.a # __all__ мы видем что доступ только к a

from package1.file1 import  d


