f = lambda x: 'Like' if x> 100 else 'Subscribe'
d = lambda x: 'Like' if x> 100 else ('Subscribe' if x >0 else 'Follow me')

print(f(10))
print(d(-1))