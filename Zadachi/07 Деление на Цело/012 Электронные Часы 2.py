## Элетронные часы 2

t = int(input())
h = (t // 3600) % 24
m1 = t // 60 % 60 // 10
m2 = t // 60 % 60 % 10
s1 = t % 60 // 10
s2 = t % 10
print(h, ":", m1, m2, ":", s1, s2, sep="")

# 2 способ решения
t = int(input())
h = (t // 3600) % 24
t = t % 3600
m = (t // 60)
if m < 10:
    m = "0" + str(m)
s = t % 60
if s < 10:
    s = "0" + str(s)
	print(h, m, s, sep=':')
# print('%d:%s:%s' % (h, m, s))
