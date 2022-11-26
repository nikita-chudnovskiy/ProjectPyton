def f(a,b,h):
    a=100
    b=200
    h.append(4)
    # print(a,b,'local') <<******** ссылки на объект



c =20
d =50
h=[1,2,3] # Т к список изменяемый объект то добавилось 4
f(c,d,h)
print(c,d,h, 'global')