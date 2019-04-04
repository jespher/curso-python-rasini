def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Jeff', False, [1, 2, 3], tamanho='M', fragil=False, sexo='M')
    todos_params(250, [25, 26, 28], 'xi', 55, segundo='Jeff', terceiro='Dir', quarto='Ulderico')
    todos_params('Junior', sobrenome='Pereira')
    todos_params(1, [4, 5], sobrenome='Pereira')
