#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# laco infinito (para quantidade infinita de situacoes)
# while True:
#     print('Infinity')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
