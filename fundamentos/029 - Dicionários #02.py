pessoa = {'nome': 'Jefferson Luis', 'idade': 30, 'cursos': ['Shell Script', 'Python']}

print(pessoa['idade'])

pessoa['cursos'].append('Ruby')
print(pessoa)

pessoa.pop('idade')  # Lê o valor e remove do dict
print(pessoa)

pessoa.update({'idade': 30, 'Sexo': 'M'})  # adiciona outros indices
print(pessoa)

del pessoa['cursos']  # deleta um indice qualquer
print(pessoa)

pessoa.clear()
print(pessoa)  # limpa o dicionário
