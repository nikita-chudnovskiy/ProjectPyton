import math
import sympy
from sympy import Symbol


def zzz(n,k):
    return math.factorial(n)//(math.factorial(k)*(math.factorial(n-k)))
z =zzz(6,3)
print(z)

n, k = map(int, input().split())
cn =(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
print(cn)

x =Symbol("x")

exp =x**2
print(exp)