def count(t,k):
    b = 0
    for i in t:
        if i == k:
            b = b+1
    return(b)
def duplicate(s):
    g = []
    for j in s:
        p = count(s,j)
        if p == 1:
            g.append(j)
    return(g)