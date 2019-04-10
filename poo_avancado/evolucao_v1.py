#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jefferson = Humano('Jefferson')
    grokn = Humano('grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jefferson.especie: {jefferson.especie}')
    print(f'grokn.especie: {grokn.especie}')
