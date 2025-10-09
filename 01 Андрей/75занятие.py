import pickle

def ceaser(text,key):
    v = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    b = text.lower()
    result = ''
    for i in b:
        if i in v:
            g = v.index(i)
            g = g+key
            if g >= 33:
                g = g-33
            result += v[g]
        else:
            result += i
    return(result)
x = ceaser('и фэщтх икхшфт',-10)
print(x)