#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8


def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(tuple(resultado))
# print(list(resultado))

# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
