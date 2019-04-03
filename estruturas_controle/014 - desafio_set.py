PALAVRAS_PROIBIDAS = {'futebol', 'política', 'religião'}
textos = [
    'Jefferson adora falar de religião e futebol',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado:', texto)

