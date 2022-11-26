a =[(i,j) for i in 'abc' for j in [1,2,3]]
print(a)

a =[i*j for i in [2,4,6,] for j in [2,4,6] ] # перемножим числа на числа и выведем если больше 10
print(a)

a =[i*j for i in [2,4,6,] for j in [2,4,6] if i*j>10 ] # перемножим числа на числа и выведем если больше 10
print(a)
