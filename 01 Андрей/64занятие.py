import random
def create(y):
    e = []
    for i in range(y):
        q = random.randint(0,100)
        e.append(q)
    return(e)
h = create(10)
print(h)
# for i in h:
#     if i > 50:
#         print(i,end=' ')

# for idx in range(0,10):
#     if h[idx] > 50:
#         print(idx,end=' ')

for idx in range(1,9):
    if h[idx] > h[idx-1] and h[idx] > h[idx+1]:
        print(h[idx],end=' ')