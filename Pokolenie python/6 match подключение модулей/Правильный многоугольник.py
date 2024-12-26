from math import pow, pi, tan

n = int(input())
a = float(input())
# S = n*(a**2)/(4*tan(pi/n))
s = n * (pow(a, 2)) / (4 * tan(pi / n))
print(s)
