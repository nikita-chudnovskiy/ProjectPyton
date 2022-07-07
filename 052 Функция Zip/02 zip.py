

numbers =[1,2,3,4]
letеers =['a','b','c','d']
symbols =['/','*','$','%']

ticked =list(zip(numbers,letеers,symbols))
print(ticked)


for t1,t2,t3 in zip(numbers,letеers,symbols):
    print('f numbers: ',{t1})
    print('f letters: ',{t2})
    print('f symbol: ',{t3})

print('************')

t1,t2,t3 =zip(*ticked)

g1=[[*t1],[*t2],[*t3]]
print(g1)