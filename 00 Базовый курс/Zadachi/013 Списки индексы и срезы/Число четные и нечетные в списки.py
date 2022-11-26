n = int(input())
i=1
a=[]
b=[]
while i<=n:
     if i%2==0:
          a.append(i)
     if i%2==1:
          b.append(i)
     i+=1
print(a)
print(b)