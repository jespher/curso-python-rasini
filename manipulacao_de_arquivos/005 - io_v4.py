try:
    arquivo = open('pessoas.csv')

    for reg in arquivo:
        print('Nome: {} Idade: {}'.format(*reg.strip().split(',')))

finally:
    print('Finally')
    arquivo.close()

if arquivo.closed:
    print('O arquivo já foi fechado!')
else:
    print('O arquivo ainda continua aberto!')
