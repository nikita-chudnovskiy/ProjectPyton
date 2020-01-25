# Найти первое и последние вхождение между ними все убрать
s = 'hello world piple hell o'
print(s.find('o'))
print(s.find('o'),s.rfind('o'))
s =s[0:5]+s[23]
print(s)