with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Name: {} idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo já foi fechado')
