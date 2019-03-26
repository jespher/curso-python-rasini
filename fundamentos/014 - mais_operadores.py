# Mais operadores

# Operador de Membro

lista = [1, 2, 3, 'Ana', 'Carla']
# print(1 in lista)
# print(5 in lista)
# print('Ana' not in lista)
# print(0 not in lista)

# operador de identidade

# x = 3
# y = x
# z = 3

# print(x is y)
# print(x is not z)
# print(x is z)
# print(y is z)
# print(y is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_a)

print(lista_c is lista_a)
print(lista_c is lista_b)

print(lista_a is not lista_c)
print(lista_b is not lista_c)

# lista_a e lista_b apontam para o mesmo endereço de memória(portanto são iguais)
# print(lista_a)
# print(lista_b)

# lista_c não está apontado para o mesmo endereço de memória que as listas 'a' e 'b'(portanto não são iguais)
# print(lista_c)

