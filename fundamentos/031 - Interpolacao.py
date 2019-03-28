from string import Template

nome, idade = 'Jefferson', 30

print('Nome: %s Idade: %d' % (nome, idade))  # versão mais antiga

print('Nome: {0} Idade: {1}'.format(nome, idade))  # dispónível até a versão do python < 3.6

print(f'Nome: {nome} Idade: {idade}')  # dispónível apartir do python >= 3.6


s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
