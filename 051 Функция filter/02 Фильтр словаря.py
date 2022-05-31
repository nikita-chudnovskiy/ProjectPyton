


a ={
    'Moskov' : 800,
    'boston' :200,
    'SF' :500
}


b = list(filter(lambda x: a[x]>200,a)) # В x будут сохранятся ключи
print(b)