arquivo = open('veiculos(meu_exemplo).csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Carro: {}, Ano: {}'.format(*registro.split(',')))
