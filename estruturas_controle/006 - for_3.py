produto = {'Nome:': 'Caneta Chique', 'Preço:': 14.99,
           'Importada:': True, 'Estoque:': 785}

# for chave in produto.keys():
#     print(chave)
#
# for valor in produto.values():
#     print(valor)

for chave, valor in produto.items():
    print(chave, valor)
