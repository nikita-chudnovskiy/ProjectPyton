a ={
    'Lidorov':{'age':1985,'hobby':'soker','car':'BMW'},
    'Ietrov':{'age':2001,'hobby':'Basketbol','car':'BMW'},
    'Kolesnikov':{'age':2002,'hobby':'Voleybol','car':'Toyota'},
    'Ehupun':{'age':2003,'hobby':'tenis','car':'BMW'},
    'Rizikov':{'age':2005,'hobby':'soker','car':'AUDI'},
    'Lustrov':{'age':2008,'hobby':'tenis','car':'Opel'},
}

b =[elem for elem in a ]
print(b)

b =[a[elem] for elem in a ] # Обращаемся по ключу
print(b)

b =[a[elem]['car'] for elem in a ] # Обращаемся по ключу Возьмем только машины Обращатся можно только к ключам кот существуют
print(b)

b =[(elem,a[elem]['car']) for elem in a if a[elem]['age']<2000 and a[elem]['hobby']=='soker'] #  Выведем фамилии и машины младше 2000 г
print(b)