#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

pessoas = [
    {'nome': 'Jefferson', 'idade': 30},
    {'nome': 'Dirlayne', 'idade': 29},
    {'nome': 'Sergio', 'idade': 52},
    {'nome': 'Leiri', 'idade': 51},
    {'nome': 'Ulderico', 'idade': 63},
    {'nome': 'Denise', 'idade': 61},
]

animal = [
    {'nome': 'Mel', 'idade': 5},
    {'nome': 'Fifi', 'idade': 20},
]

menores = filter(lambda p: p['idade'] < 18, animal)
print(list(menores))

maiores = filter(lambda p: p['idade'] > 18, animal)
print(list(maiores))

maiores = filter(lambda p: p['idade'] > 18, pessoas)
print(list(maiores))

nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(nomes_grandes))

