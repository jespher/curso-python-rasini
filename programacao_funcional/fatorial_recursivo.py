#!C:\Users\Denis\AppData\Local\Programs\Python\Python37
# coding=utf8

def fatorial(n):
    return n * (fatorial(n -1) if (n - 1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
