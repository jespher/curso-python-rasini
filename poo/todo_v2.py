from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __add__(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.__add__('Passar roupa')
    casa.__add__('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'-{tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.__add__('Frutas')
    mercado.__add__('carne')
    mercado.__add__('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'-{tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()