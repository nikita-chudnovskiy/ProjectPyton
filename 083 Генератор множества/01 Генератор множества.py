may_set ={i for i in range(1,6)}
print(may_set)

may_set ={i for i in [1,1,2,2,3,3,0,0,0,0]}
print(may_set,type(may_set))


print()
my_set ={i+j for i in 'aaa' for j in 'def'}
my_list =[i+j for i in 'aaa' for j in 'def']

# Наглядный пример множеств убирать дубли
print(my_set,type(may_set))
print(my_list,my_set)

print()

#(Можем создавать и кортежи !!!!) (Списки нельзя !! {[i,j])}
my_set1 ={(i,j) for i in 'aaa' for j in 'de'}
my_list1 =[(i,j) for i in 'aaa' for j in 'de']
print(my_set1)
print(my_list1)

