n = int(input())
i=1
a=[]
while n>=i//2:
     if n%i==0:
          a.append(i)
     i+=1
print(a)