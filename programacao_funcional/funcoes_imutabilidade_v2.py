#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

from functools import reduce
from operator import add

valores = (30, 10, 25, 55, 5, 8, 965, 87, 99, 65, 38)

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)
