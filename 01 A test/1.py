
a =[('Вася',18),
    ('Федя',19),
    ('Васек',20)
    ]




b = [i for i in a if i[0].startswith('В') and i[1]<19 ]
print(b)

print()
a ={
    'Васek':{'age':19,'auto':'BMW'},
    'Вася':{'age':17,'auto':'BMW'},
    'ФЕДЯ':{'age':20,'auto':'Marsedes'},
    'Коля':{'age':21,'auto':'Shkoda'},

    }


b = [(i,a[i]['auto']) for i in a if a[i]['age']>18 and a[i]['auto']=='BMW' ]
print(b)