import libra as l


#import importlib
from importlib import reload
print(l.my_str)

l.my_str ='ZZZZ'
print(l.my_str)

reload(l)

print(l.my_str)

