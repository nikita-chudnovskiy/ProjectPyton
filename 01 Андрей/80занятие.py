# k = 2
# for i in range(178):
#     k = k*2
# print(k)

# g = 1
# for i in range(2,20+1):
#     g = g*i
# print(g)

# g = 1
# for b in range(2,1000+1):
#     g = g+b
# print(g)

# A = int(input())
# B = int(input())
# for i in range(A,B+1):
#     print(i,end=' ')

# A = int(input())
# B = int(input())
# if A < B:
#     for i in range(A,B+1):
#         print(i,end=' ')
# else:
#     for i in range(A,B-1,-1):
#         print(i,end=' ')

d = 1
n = int(input())
for i in range(2,n+1):
    d = d+i*i
print(d)