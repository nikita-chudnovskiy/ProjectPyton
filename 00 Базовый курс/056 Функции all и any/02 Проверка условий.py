
#a = 100
a=99 # all уже не будет подходить и выдаст false так как 1 условие не выполняется
condition_1 = a%2==0
condition_2 = a>50
condition_3 = a<1000

print(all([condition_1,condition_2,condition_3]))
print(any([condition_1,condition_2,condition_3]))




#a = 100
a=1 # all уже не будет подходить и выдаст false
condition_1 = a%2==0
condition_2 = a>50
condition_3 = a>1000

print(all([condition_1,condition_2,condition_3]))
print(any([condition_1,condition_2,condition_3]))

print('функции any все 3 условия не выполняются')