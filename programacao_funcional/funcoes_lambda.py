#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 4, 'preco': 30},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais:', totais)
print('Total geral:', sum(totais))
