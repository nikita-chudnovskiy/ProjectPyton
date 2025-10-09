g = int(input())
b = int(input())
a = int(input())
if b <= a and a <= g:
    print(b,a,g)
elif a <= g and g <= b:
    print(a,g,b)
elif g <= a and a <= b:
    print(g,a,b)
elif a <= b and b <= g:
    print(a,b,g)
elif g <= b and b <= a:
    print(g,b,a)
elif b <= g and g <= a:
    print(b,g,a)