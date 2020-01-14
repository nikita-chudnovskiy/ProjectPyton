h1,m1,s1= map(int,input().split())
h2,m2,s2= map(int,input().split())
h1=h1*3600
m1 =m1*60
s1 = s1*1

h2=h2*3600
m2 =m2*60
s2 = s2*1

vremya1 =h1+m1+s1
vremya2 =h2+m2+s2
raznica = vremya2-vremya1
print(raznica)