a =[1,1,2,3,4,4,5,6,7,8,8,8,3,9]
count =[0]*10
for i in a:
    count[i]+=1
for i in range(len(count)):
    if count[i]>0:
        # print(i,count[i])
        print((str(i) + ' ') * count[i], end=' ')
