my_list =[1,2,3,4]


second_list =my_list
my_list.append(100)
print(id(second_list),second_list,id(my_list),my_list) # id так не меняется , а если скопируем то поменяется

new = my_list.copy()  # а если скопируем то поменяется
new.append(999)
print(id(new),new)



# Не изменяемые объекты это числа и строки (меняется id если мы изменяем, создается новый объект)
valve=42
massa =valve
print(valve,massa)
massa+=1
print(valve,massa)


a =['hello']
print(id(a))
a[0]='bay'
print(id(a))



solder ='knight'
knight = solder
knight=knight+'_shlem'
print(id(solder),solder)
print(id(knight),knight)