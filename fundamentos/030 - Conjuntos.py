# Conjunto

# a = {1, 2, 3}
# print(a)
# print(type(a))

# print(a[0]) não funciona

# b = set('cod3r')
# print(b)

# teste = '3' in a, 4 not in a
# print(teste)

# teste2 = {1, 2, 3} == {3, 2, 1, 3}
# print(teste2)

# operações

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))  # Cria a união de c1 e c2

print(c1.intersection(c2))  # Cria a intercecção de c1 e c2

print(c1.update(c2))

print(c1)

print(c2)

print(c2 <= c1)

print(c2 >= c1)

print({1, 2, 3} - {2})
print({1, 2, 3} - {1, 3})

c1 -= {3}
print(c1)
