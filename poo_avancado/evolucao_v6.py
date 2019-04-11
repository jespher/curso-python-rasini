#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
from abc import ABCMeta, abstractmethod


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @abstractmethod
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    try:
        anonimo = Humano('Jeff Lui')
        print(anonimo.inteligente)
    except TypeError:
        print('classe abstrata')

    jefferson = HomoSapiens('Jefferson')
    print('{} da classe {}, inteligente: {}'
          .format(jefferson.nome,
                  jefferson.__class__.__name__,
                  jefferson.inteligente))

    grong = Neanderthal('Grong')
    print('{} da classe {}, inteligente: {}'
          .format(grong.nome,
                  grong.__class__.__name__,
                  grong.inteligente))
