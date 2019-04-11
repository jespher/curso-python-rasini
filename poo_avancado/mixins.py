#!C:\Users\Denis\AppData\Local\Programs\Python\Python37

class HtmlToStringMixin:
    def __str__(self):
        # conversao para html
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet) ' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Jefferson Luis')
    print(p1)

    p2 = PessoaHtml('Dirlayne Rasini')
    print(p2)

    dog = AnimalHtml('Mel')
    print(dog)
