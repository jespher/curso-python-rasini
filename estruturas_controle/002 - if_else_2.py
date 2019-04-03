def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'idade invalida'


if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -5, 57, 99, 0):
        print(f'{idade}: {faixa_etaria(idade)}')
