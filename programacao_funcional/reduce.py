#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8
from functools import reduce

pessoas = [
    {'nome': 'Jefferson', 'idade': 30},
    {'nome': 'Dirlayne', 'idade': 29},
    {'nome': 'Sergio', 'idade': 52},
    {'nome': 'Leiri', 'idade': 51},
    {'nome': 'Ulderico', 'idade': 63},
    {'nome': 'Denise', 'idade': 61},
]

so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade > 18, so_idades)

soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades)
