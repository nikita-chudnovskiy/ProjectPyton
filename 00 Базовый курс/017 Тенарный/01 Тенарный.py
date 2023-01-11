a =-2
b =-7
print("да" if a ==2 else "нет")

my_f =lambda i: f"Больше равно {i}" if i >=3 else "меньше"
print(my_f(3))
print(my_f(10))


res = a+2 if a>2 else b-4 # b-4
print(res)

res = abs(a) if a>2 else abs(b) # b-4
print(res)


# Очень интересно

s ='python'
t = "upper"

res = s.upper() if  t =="upper" else s
print(res)

res  = f"a  {a} "+("четное" if a%2==0 else "не четное")+ " число"
print(res)