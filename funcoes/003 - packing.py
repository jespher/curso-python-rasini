def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    # packing
    print(soma_n(1))
    print(soma_n(2, 3))
    print(soma_n(1, 1, 1, 2, 3, 4, 5))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_n(*tupla_nums))
    lista_nums = [1, 2, 5]
    print(soma_n(*lista_nums))
