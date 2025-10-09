# b = []
# for i in range(6):
#     k = int(input())
#     b.append(k)
# for idx in range(1,5):
#     if b[idx-1] == b[idx+1]:
#         print(b[idx])

# h = []
# for i in range(6):
#     y = int(input())
#     h.append(y)
# for idx in range(1,5):
#     if h[idx-1] + h[idx+1] == h[idx]:
#         print(h[idx])

s = []
for i in range(5):
    e = int(input())
    s.append(e)
for idx in range(0,5):
    if s[idx+1] == max(s):
        print(s[idx])