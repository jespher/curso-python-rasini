# Dicionário

pessoa = {'nome': 'Prof(a). Denise',
          'Idade': 38,
          'cursos': ['Inglês', 'Português'],
          'Alunos': ['Jefferson', 'Dirlayne']}

print(type(pessoa))

# print(dir(dict))

print(len(pessoa))

print(pessoa['nome'])

print(pessoa['Idade'])

print(pessoa['cursos'])

print(pessoa['cursos'][0])
print(pessoa['cursos'][1])

print(pessoa['Alunos'])
print(pessoa['Alunos'][0])
print(pessoa['Alunos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('Idade'))
print(pessoa.get('Alunos'))
print(pessoa.get('Alunos')[0])
print(pessoa.get('Alunos')[1])

print(pessoa.get('cursos'))
print(pessoa.get('cursos')[0])
print(pessoa.get('cursos')[1])

print(pessoa.get('tags'))
print(pessoa.get('tags', []))


