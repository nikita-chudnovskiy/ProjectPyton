s ="""hello
world"""
print(s)

a ='abc\ndeg'
print(a)
print(len(a))# Служебный символ \n считает за один

a ='fff\nggg\tjjj\nooo' # если поставить r перед кавычками  'fff\nggg\tjjj\nooo' никакого форматирования не произойдет
print(a)




a ='f\ng\tj\no'
print(a)
print(len(a))
a =r'f\n\tj\no'
print(a)
print(len(a))

print('C:\\default')

# r Будет убирать все служебные символы в этой строке