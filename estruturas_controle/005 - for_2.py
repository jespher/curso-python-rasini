palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end='\n')
print('Fim')


# -------------------------------------------------------------------------------------------------

aprovados = ['Jefferson', 'Derico', 'Dirlayne', 'Denise', 'Sergio', 'Leiri', 'Lilian', 'Pedro', 'Giuliano', 'Felipe']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# ------------------------------------------------------------------------------------------------

dias_semana = ('Domingo', 'Segunda', 'Terça'
                                     'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('jeffersonluisrasini'):
    print(letra)

for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
    print(numero)
