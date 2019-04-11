#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 4, 'preco': 30},
)


def calc_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calc_preco_total, compras))

print('Preços totais:', totais)
print('Total geral:', sum(totais))
