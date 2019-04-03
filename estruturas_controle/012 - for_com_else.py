lista_palavras = ['futebol', 'política', 'religião']
PALAVRAS_PROIBIDAS = {'futebol', 'política', 'religião'}
textos = [
    'Jefferson adora falar de religião e futebol',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break

    else:
        print('Texto autorizado:', texto)
