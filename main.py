import package1.file1
from package1 import file2 # Теперь не нужно писать  package2.file2.a
from package1.file2 import c  # Обращаемся уже напрямую

print(package1.file1.d)
print(file2.a)
print(c)

