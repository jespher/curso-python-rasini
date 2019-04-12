#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

from generators_v1 import cores_arco_iris

if __name__ == '__main__':
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim!')
