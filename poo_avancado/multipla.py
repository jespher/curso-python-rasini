#!C:\Users\Denis\AppData\Local\Programs\Python\Python37

class Animal:
    @property
    def capacidades(self):
        return 'dormir', 'comer', 'correr', 'beber'


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class SpdMn(Aranha, Homem):
    @property
    def capacidades(self):
        return super().capacidades + \
               ('bater em bandidos', 'atirar teias entre predios')


if __name__ == '__main__':
    jeff = Homem()
    print(f'Jeff: {jeff.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    peter = SpdMn()
    print(f'Peter Parker: {peter.capacidades}')
