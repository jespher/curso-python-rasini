with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Name: {} Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O arquivo já foi fechado')

if saida.closed:
    print('A saída está fechada')
